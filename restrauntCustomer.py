from SPXCafe2 import SPXCafe
from Avatar2 import Avatar
class tenOutOfTenCustomer(SPXCafe):

    def __init__(self):
        '''Constructor method'''
        self.SuperWaiter = Avatar("SuperBot")
        self.cafe = SPXCafe()

    def greetings(self):
        '''login or signup options'''
        #inpNewOrReturning = self.SuperWaiter.listen("Please say Login if you want to Login, say sign up if you are new")
        while True:
            self.SuperWaiter.say("Do you want to enter or 'Exit' ")
            inpNewOrReturning = input("Do you want to 'enter' or 'Exit' ").lower() # CHANGE TO WAITER SAYING THIS AND FUZZY
            if inpNewOrReturning == "enter":
                return self.getCusotmerLoginOrSignUp()
            elif inpNewOrReturning == "exit":
                return self.exitCustomer()
            else:
                self.SuperWaiter.say("Please try again")

    def getCusotmerLoginOrSignUp(self):
        '''login or signup'''
        signedUp = False
        self.SuperWaiter.say("Please enter your username: ")
        userName = input("Please enter your username: ").lower() # for accuracy
        self.setUserName(userName) # sets username
        if self.existsDBUserName(): # checks if username in database to prevent overlapping 
            self.setCustomer(userName)
            self.SuperWaiter.say(f"Welcome back to TenOutOfTenRestraunt by Cree gaming, {self.getFirstName()} {self.getLastName}!")
            signedUp = True
        else:
            firstName = self.SuperWaiter.say("Please enter your first name: ")
            firstName = input("Please enter your first name: ").lower() # asks first Name
            self.setFirstName(firstName)                                # sets first Name
            self.SuperWaiter.say("Please enter your last name: ")       
            lastName = input("Please enter your last name: ").lower()   # asks last name .lower()
            self.setLastName(lastName)                                  # sets last name
            self.saveCustomer()                                         # adds users to database (saves)
            self.SuperWaiter.say(f"Welcome to TenOutOfTenRestraunt by Cree gaming, {firstName.title()} {lastName.title()}!") #Welcomes customer
            signedUp = True # ends signup loop
        # print("Finished signup")
        return signedUp

    def existsDBUserName(self):
        '''check if object already exists in datbase'''
        retcode = False
        sql =None
        if self.getUserName():
            sql = f'''SELECT count(*) AS count FROM Customers WHERE userName = '{self.getUserName()}' ''' #sql checks for amount of usernames in database
            # print(sql)
        if sql:
            countData = self.cafe.dbGetData(sql)
            # print(countData)
            if countData:
                for countRec in countData: 
                    print(countRec)
                    count  = int(countRec['count'])
                if count >0:
                    retcode = True
        return retcode  #Returns True for if statements to check if database
    
    def saveCustomer(self): # Saves login data
        '''saves the signup data into record and if changes in names and stuff'''
        if self.existsDBUserName():     # for changing username and stuff will see to it later!!!
            sql = f'''UPDATE customers SET
                customerId = {self.getCustomerId()},
                userName = '{self.getUserName()}',
                firstName = '{self.getFirstName()}',
                lastName = '{self.getLastName()}'
            WHERE customerId={self.getCustomerId()}'''
            self.cafe.dbChangeData(sql)
        else:
            sql = f'''INSERT INTO customers (userName, firstName, lastName) VALUES
                ('{self.getUserName()}','{self.getFirstName()}','{self.getLastName()}')'''
            print(sql)
            self.customerId = self.cafe.dbPutData(sql)
            # self.setCustomerID(self.dbPutData(sql))

    def exitCustomer(self):
        print("Thank you for coming TenOutOfTenRestraunt we hope to see you again")
        self.SuperWaiter.say("Thank you for coming TenOutOfTenRestraunt we hope to see you again")
        return False

# Getters/Setters
    def setCustomer(self, userName= None, customerId = None): # will have to get customer Id
        '''use this to get customer id for orders !!!!!!  '''
        customerData = None
        if self.getUserName():
            sql  =f'''
                SELECT customerId, userName, firstName, lastName
                FROM customers
                WHERE userName = '{self.getUserName()}'
                ORDER BY customerId
                '''
        customerData = self.cafe.dbGetData(sql)
        if customerData:
            #Eiting customer = should only be one customer
            for customer in customerData:
                self.customerId = customer['customerId']         #grabs the customer data from database into a variable
                self.userName = customer['userName']
                self.firstName = customer['firstName']
                self.lastName = customer['lastName']
                # Call ORDER factory method to return a list of order objects/instances - pass self to it
                # self.setORders(Order.getORders(self))
                retcode = True
        self.setFirstName(self.firstName)
        self.setLastName(self.lastName)
        self.setCustomerId(self.customerId)

        return retcode

    def setFirstName(self, firstName = None):
        self.__firstName= firstName
    def setLastName(self, lastName = None):
        self.__lastName= lastName
    def setUserName(self, userName= None):
        self.__userName= userName
    def setCustomerId(self, customerId=None):
        self.__customerId=customerId
    def getCustomerId(self):
        return self.__customerId  
    def getFirstName(self):
        return self.__firstName
    def getLastName(self):
        return self.__lastName
    def getUserName(self):
        return self.__userName
def main():
    '''test harness'''
    customer= tenOutOfTenCustomer()
    customer.getCusotmerLoginOrSignUp()
    print(customer.getCustomerId())
    print(customer.getFirstName())
    print(customer.getLastName())
    print(customer.getUserName())
if __name__=="__main__":
    main()
# Notes
    #     '''Creates customer Object from database info
    #     arguments: either userName or cusomter Ide'''
    #     retcode = False
    #     if userName:
    #         self.setUserName(userName)
    #     if customerId:
    #         self.setCustomerId(customerId)
    #     customerData =None
    #     if self.getCustomerId(): # customer must exist
    #         sql = f'''
    #             SELECT customerId, userName, firstName, lastName
    #             FROM custumers
    #             WHERE customerId = {self.getCustomerId()}
    #             ORDER BY customerId'''
    #     # eithernew cusotmer orexisting get useoing username
    #     elif self.getUserName():
    #         sql  =f'''
    #             SELECT customerId, userName, firstName, lastName
    #             FROM customers
    #             WHERE userName = '{self.getUserName()}'
    #             ORDER BY customerId
    #             '''
    #     customerData = self.dbGetData(sql)
    #     if customerData:
    #         #Eiting customer = should only be one customer
    #         for cusomter in customerData:
    #             self.customerId = customer['customerId']
    #             self.userName = customer['userName']
    #             self.firstName = customer['firstName']
    #             self.lastName = customer['lastName']
    #             # Call ORDER factory method to return a list of order objects/instances - pass self to it
    #             # self.setORders(Order.getORders(self))
    #             retcode = True
    #     return retcode
        # def login(self):
    #     print("login")
    #     login = False
    #     self.SuperWaiter.say("Please enter your username: ")
    #     userName = input("Please enter your username: ").lower()    # for accuracy
    #     self.setUserName(userName)
    #     if self.existsDBUserName(): # checks if username is in database
    #         login = True
    #     else:                       # Person only has one chance to get their username right
    #         print("Username incorrect!")
    #         self.SuperWaiter.say("Your UserName is incorrect!")
    #         self.SuperWaiter.say("Redirecting to signUp")
    #         self.signUp()
    #     return login
