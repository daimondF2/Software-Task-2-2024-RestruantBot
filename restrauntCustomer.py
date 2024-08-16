from SPXCafe2 import SPXCafe
from Avatar2 import Avatar
import orderItems
import orderDb
class tenOutOfTenCustomer(SPXCafe):

    def __init__(self, userName=None, firstName=None, lastName =None, customerId = None):
        '''Constructor method'''
        super().__init__()
        self.SuperWaiter = Avatar("tenOutOfTenRestaurant Bot")
        self.setCustomerId(customerId=customerId)

    def getCusotmerNewOrReturning(self):
        '''login or signup'''
        signedUp = False
        self.SuperWaiter.say("Please enter your username: ")
        userName = input("Please enter your username: ").lower() # for accuracy
        self.setUserName(userName) # sets username
        if self.existsDBUserName(): # checks if username in database to prevent overlapping 
            self.setCustomer()
            self.SuperWaiter.say(f"Welcome back to TenOutOfTenRestraunt by Cree gaming, {self.getFirstName()} {self.getLastName()}!")
            signedUp = True
        else:
            firstName = self.SuperWaiter.say("Please enter your first name: ")
            firstName = input("Please enter your first name: ").lower() # asks first Name
            self.setFirstName(firstName)                                # sets first Name
            self.SuperWaiter.say("Please enter your last name: ")       
            lastName = input("Please enter your last name: ").lower()   # asks last name .lower()
            self.setLastName(lastName)                                  # sets last name
            self.saveCustomer() 
            self.setCustomer()                                        # adds users to database (saves)
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
            countData = self.dbGetData(sql)
            # print(countData)
            if countData:
                for countRec in countData: 
                    # print(countRec)
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
            self.dbChangeData(sql)
        else:
            sql = f'''INSERT INTO customers (userName, firstName, lastName) VALUES
                ('{self.getUserName()}','{self.getFirstName()}','{self.getLastName()}')'''
            print(sql)
            self.customerId = self.dbPutData(sql)
            # self.setCustomerID(self.dbPutData(sql))

    def newOrder(self, basket=None):
        '''connects to orders to create order'''
        trolley = basket
        if basket:
            self.order = orderItems.orderItems(customer=self)
            self.orderHS = orderDb.orderDb(self.getCustomerId())
            self.orderHS.createOrder(customerId=self.getCustomerId(), basket=trolley)
        else:
            return self.SuperWaiter.say("Please try again.")
        
    def history(self):
        '''connects to orderhistory to check history'''
        self.orderHS = orderDb.orderDb(self.getCustomerId())
        if self.orderHS.existDbOrder(self.getCustomerId()):
            self.orderHS.setOrder()
        else:
            self.SuperWaiter.say("You have had no previous orders with us.")

    def exitCustomer(self):
        '''customer exit'''
        print("Thank you for coming TenOutOfTenRestraunt we hope to see you again")
        self.SuperWaiter.say("Thank you for coming TenOutOfTenRestraunt we hope to see you again")
        return False

# Getters/Setters
    def setCustomer(self): # will have to get customer Id
        '''use this to get customer id for orders !!!!!!  '''
        customerData = None
        if self.getUserName():
            sql  =f'''
                SELECT customerId, userName, firstName, lastName
                FROM customers
                WHERE userName = '{self.getUserName()}'
                ORDER BY customerId
                '''
        customerData = self.dbGetData(sql)
        if customerData:
            #Eiting customer = should only be one customer
            for customer in customerData:
                self.customerId = customer['customerId']         #grabs the customer data from database into a variable
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
    def setCustomerId(self, customerId= None):
        self.__customerId = customerId
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
    customer= tenOutOfTenCustomer(1)
    customer.history()

    # customer.getCusotmerNewOrReturning()
    # customer.newOrder()
if __name__=="__main__":
    main()
