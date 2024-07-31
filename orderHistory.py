from SPXCafe2 import SPXCafe
from restrauntCustomer import tenOutOfTenCustomer
class orderHistor(SPXCafe):
    def __init__(self):
        super().__init__()
        self.customerInfo = tenOutOfTenCustomer()
        self.getToday()
        # orderDate = datetime.today().strftime("%Y-%m-%d")
        self.addOrders()



    def addOrders(self):
        # adds orders to order history
        pass
    def seeOrderHistory(self):
        sql =None
        if self.customerInfo.getCustomerId():
            sql = f'''SELECT orderId, orderDate, customerId 
            FROM Orders 
            WHERE customerId = '{self.customerInfo.getCustomerId()}'
            ORDER BY orderId
            '''
            print(sql)
            orderHSdata = self.dbGetData(sql)
        if orderHSdata:
            for orders in orderHSdata:
                self.orderId =
                self.userName = customer['userName']
                self.firstName = customer['firstName']
                # Call ORDER factory method to return a list of order objects/instances - pass self to it
                # self.setORders(Order.getORders(self))
                retcode = True
        self.setFirstName(self.firstName)
        self.setLastName(self.lastName)
        self.setCustomerId(self.customerId)

            
            print(orderHSdata)
    # You must be able to allow the customer to access their previous orders, including
    # Order number
    # Order Date
        pass

    def existDb(self):
        '''check if object already exists in datbase'''
        retcode = False
        sql =None
        if self.getUserName():
            sql = f'''SELECT count(*) AS count FROM Orders WHERE customerId = '{self.customerInfo.getCustomerId()}' ''' #sql checks for amount of usernames in database
            # print(sql)
        if sql:
            countData = self.dbGetData(sql)
            # print(countData)
            if countData:
                for countRec in countData: 
                    print(countRec)
                    count  = int(countRec['count'])
                if count >0:
                    retcode = True
        return retcode


    def displayOrderHistory(self):
        pass
    
    # For Previous Orders

# The Meals/Dishes ordered and their prices (at that point in time)
# Total order value