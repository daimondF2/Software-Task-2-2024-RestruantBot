from SPXCafe2 import SPXCafe
from restrauntCustomer import tenOutOfTenCustomer
from Avatar2 import Avatar
class orderHistory(SPXCafe):
    def __init__(self):
        super().__init__()
        self.customerInfo = tenOutOfTenCustomer()
        self.SuperCustomer = Avatar("tenOutOfTenRestaurant Bot")
        self.getToday()
        # orderDate = datetime.today().strftime("%Y-%m-%d")
        self.addOrders()

    def addOrders(self):
        # adds orders to order history
        pass

    def findOrderHistory(self, customerId= None):
        sql =None
        h= True
        # if self.customerInfo.getCustomerId():
        if h ==True:
            sql = f'''SELECT orderId, orderDate, customerId 
            FROM Orders 
            WHERE customerId = '{customerId}'
            ORDER BY orderId
            '''
            print(sql)
            orderHSdata = self.dbGetData(sql)
            print(orderHSdata)
        if orderHSdata:
            for orders in orderHSdata:
                self.orderId = orders['orderId']
                self.orderDate = orders['orderDate']
                self.customerId = orders['customerId']
                self.setOrderId(self.orderId)
                self.setOrderDates(self.orderDate)
                self.setCustomerId(self.customerId)
                print(self.getOrderId())
                print(self.getOrderDates())
                print(self.getCustomerId())
                # Call ORDER factory method to return a list of order objects/instances - pass self to it
                retcode = True
        
            
        # print(orderHSdata)
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
    
    # For Previous Order
# The Meals/Dishes ordered and their prices (at that point in time)
# Total order value

# getters/ setters
    def setOrderId(self, orderId=None):
        self.__orderId = orderId
    def getOrderId(self):
        return self.__orderId
    def setOrderDates(self, orderDate=None):
        self.__orderDate = orderDate
    def getOrderDates(self):
        return self.__orderDate
    def setCustomerId(self, customerId=None):
        self.__customerId = customerId
    def getCustomerId(self):
        return self.__customerId
    
def main():
    orderHs= orderHistory()
    orderHs.findOrderHistory(customerId=1)
if __name__ == "__main__":
    main()