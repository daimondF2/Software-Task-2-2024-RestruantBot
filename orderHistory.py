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
        # self.addOrders()

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
                self.findOrderFood()
                # Call ORDER factory method to return a list of order objects/instances - pass self to it
                retcode = True
        
        # print(orderHSdata)
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
        print(f"orderId: {self.getOrderId()}| orderDate: {self.getOrderDates()} | customerId: {self.getCustomerId()}| mealId: {self.getMealId()}| quantity: {self.getQuantity()}")

    def findOrderFood(self):
        sql =None
        sql = f'''SELECT orderItemId, orderId, mealId, quantity, mealPrice 
            FROM orderItems 
            WHERE orderId = '{self.getOrderId()}'
            ORDER BY orderItemId
            '''
        orderData = self.dbGetData(sql)
        for items in orderData:
            self.orderItemId = items['orderItemId']
            self.mealId = items['mealId']
            self.quantity = items['quantity']
            self.mealPrice = items['mealPrice']
            self.setOrderItemId(self.orderItemId)
            self.setMealId(self.mealId)
            self.setQuantity(self.quantity)
            self.displayOrderHistory()

    # For Previous Order
# The Meals/Dishes ordered and their prices (at that point in time)
# Total order value

# getters/ setters
    def setOrderItemId(self, orderItemId=None):
        self.__orderItemId = orderItemId
    def getOrderItemId(self):
        return self.__orderItemId
    def setMealId(self, mealId = None):
        self.__mealId = mealId
    def getMealId(self):
        return self.__mealId
    def setQuantity(self, quantity=None):
        self.__quantity= quantity
    def getQuantity(self):
        return self.__quantity
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