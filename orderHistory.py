from SPXCafe2 import SPXCafe
from Avatar2 import Avatar
class orderHistory(SPXCafe):
    def __init__(self):
        '''Constructor '''
        super().__init__()
        self.SuperCustomer = Avatar("tenOutOfTenRestaurant Bot")
        self.getToday()
        self.totalPrice = 0
        print("---------------------- Past Orders ----------------------")

    def findOrderHistory(self, customerId=None):
        '''gets order ids and all orders made by customer'''
        sql =None
        if customerId:
            sql = f'''SELECT orderId, orderDate, customerId 
            FROM Orders 
            WHERE customerId = '{customerId}'
            ORDER BY orderId
            '''
            # print(sql)
            orderHSdata = self.dbGetData(sql)
            # print(orderHSdata)
        if orderHSdata:
            for orders in orderHSdata:
                self.orderId = orders['orderId']
                self.orderDate = orders['orderDate']
                self.customerId = orders['customerId']
                self.setOrderId(self.orderId)
                self.setOrderDates(self.orderDate)
                self.setCustomerId(self.customerId)
                # print(self.getOrderId())
                # print(self.getOrderDates())           checks if they worked
                # print(self.getCustomerId())
                self.findOrderFood()
                # Call ORDER factory method to return a list of order objects/instances - pass self to it
        print(f"| Total price: {self.totalPrice} |") # displays total cost
        
    def existDbHistory(self, customerId=None):
        '''check if object already exists in datbase'''
        retcode = False
        sql =None
        if self.getUserName():
            sql = f'''SELECT count(*) AS count FROM Orders WHERE customerId = '{customerId}' ''' #sql checks for amount of usernames in database
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
        '''Displays Order Data'''
        # print(f"orderId: {self.getOrderId()}| orderDate: {self.getOrderDates()} | customerId: {self.getCustomerId()}| mealId: {self.getMealId()}| quantity: {self.getQuantity()}| meal: {self.__mealName}| price: {self.__mealPrice}")
        print(f"| orderDate: {self.getOrderDates()} | meal: {self.__mealName} | quantity: {self.getQuantity()} |  price: {self.__mealPrice} |")

    def findOrderFood(self):
        '''Finds the orders from orderId'''
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
            self.__mealPrice = items['mealPrice']
            self.setOrderItemId(self.orderItemId)
            self.setQuantity(self.quantity)
            self.setMealId(self.mealId)
            self.totalPrice += int(self.getQuantity())*int(self.__mealPrice) # gets total price of meal
            # print(f"total price: {self.totalPrice}")
            self.findFood()

    def findFood(self):
        '''gets the meal name form mealId'''
        sql = None
        sql = f'''SELECT mealId, mealName, mealPrice, courseId 
            FROM meals 
            WHERE mealId = '{self.getMealId()}'
            ORDER BY mealId
            '''
        mealData = self.dbGetData(sql)
        for meals in mealData:
            self.__mealName = meals['mealName']
            self.displayOrderHistory()

# getters/ setters
    def setOrderItemId(self, orderItemId=None):
        self.__orderItemId = orderItemId
    def getOrderItemId(self):
        return self.__orderItemId
    def setQuantity(self, quantity=None):
        self.__quantity= quantity
    def getQuantity(self):
        return self.__quantity
    def setMealId(self, mealId=None):
        self.__mealId = mealId
    def getMealId(self):
        return self.__mealId
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
    '''test harness'''
    orderHs= orderHistory()
    orderHs.findOrderHistory(customerId=1)
if __name__ == "__main__":
    main()