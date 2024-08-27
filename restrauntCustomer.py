from SPXCafe2 import SPXCafe
from Avatar2 import Avatar
import orderItems
import orderDb
class tenOutOfTenCustomer(SPXCafe):

    def __init__(self, userName=None, firstName=None, lastName =None, customerId = None):
        '''Constructor method'''
        super().__init__() #inheritence 
        self.SuperWaiter = Avatar("tenOutOfTenRestaurant Bot")
        self.setCustomerId(customerId=customerId)
        self.__basket = [] # basket stuff
        self.setUserName(userName)
        self.setFirstName(firstName)
        self.setLastName(lastName)
        if self.existsDBUserName():
            self.setCustomer()

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
            # print(sql)
            self.customerId = self.dbPutData(sql)
            # self.setCustomerID(self.dbPutData(sql))


    def displayOrderHistory(self):
        '''connects to orderhistory to check history'''
        print("|---------------------- Past Orders ----------------------|")
        for orders in self.getOrderHistory():
            total = 0
            print(f"Order Date: {orders.getOrderDates()}")
            for orderitems in orders.getAllOrder():
                orderitems.display()
                total += orderitems.getMealPrice() * orderitems.getQuantity()
            print(f"Order total: {total}")
            print("-"*38)

        # if self.orderHS.existDbOrder(customerId=self.getCustomerId()):
        #     for orders in self.getOrderHistory():
        #         orders.display()
        # else:
        #     self.SuperWaiter.say("You have had no previous orders with us.")

    def displayBasket(self, basket=None):
        '''Displays basket'''
        totalOrderPrice = 0
        print("|--------------------- Order ---------------------|")
        for orderItems in self.getBasket():
            totalPrice = 0
            mealData = orderItems[0]
            totalPrice += int(mealData[1])*int(orderItems[1])
            totalOrderPrice +=totalPrice
            print(f"Meal: {orderItems[2]} | Quantity: {orderItems[1]} | Total Price: {totalPrice} | Single Meal Price: {mealData[1]}")
        print(f"| Total Order Price: {totalOrderPrice} |")

    def checkOut(self):
        '''checkOut system'''
        customerOrder = self.getBasket()
        self.displayBasket()
        # orderConfirm = self.SuperWaiter.listen("Would you like to confirm Order? ").lower()
        orderConfirm =input("yes? ")
        if orderConfirm == "yes" or "yeh":
            self.orderHS.createOrder(customerId=self.getCustomerId(), basket=self.getBasket())

# Getters/Setters
    def setCustomer(self, userName = None, userId =None): # will have to get customer Id
        '''use this to get customer id for orders !!!!!!  '''
        customerData = None
        if self.getUserName():
            sql  =f'''
                SELECT customerId, userName, firstName, lastName
                FROM customers
                WHERE userName = '{self.getUserName()}'
                ORDER BY customerId
                 '''
        elif userName:
            sql = f'''
                SELECT customerId, userName, firstName, lastName
                FROM customers
                WHERE userName = '{userName}'
                ORDER BY customerId
                '''
        # print(sql)
        customerData = self.dbGetData(sql)
        # print(customerData)
        if customerData:
            #Eiting customer = should only be one customer
            for customer in customerData:
                self.customerId = customer['customerId']         #grabs the customer data from database into a variable
                self.firstName = customer['firstName']
                self.lastName = customer['lastName']
                # Call ORDER factory method to return a list of order objects/instances - pass self to it
                # self.setORders(Order.getORders(self))
        self.setFirstName(self.firstName)
        self.setLastName(self.lastName)
        self.setCustomerId(self.customerId)
        self.orderHS = orderDb.orderDb(customerId=self.getCustomerId())
        self.setOrderHistory(self.orderHS.getOrders(self.getCustomerId()))
        return self.getCustomerId()

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
    def setBasket(self, meal, quantity, mealName):
        self.__basket.append([meal, quantity, mealName])
    def getBasket(self):
        return self.__basket
    def delBasket(self):
        self.__basket = []
    def setOrderHistory(self, orders = None):
        if orders:
            self.__orders = orders
        else:
            self.__orders = []
    def getOrderHistory(self):
        return self.__orders

def main():
    '''test harness'''
    customer= tenOutOfTenCustomer()
    customer.setCustomer(userName='diamondf')
    # customer.setBasket(meal="steak",quantity=3)
    # customer.setBasket(meal='streak',quantity=2)
    # print(customer.getBasket())
    # customer.setCustomer('diamondf')
    # customer.displayBasket()
    customer.displayOrderHistory()
    # customer.newOrder()

    # customer.getCusotmerNewOrReturning()
    # customer.newOrder()
if __name__=="__main__":
    main()
