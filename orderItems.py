from SPXCafe2 import SPXCafe
from Avatar2 import Avatar
import menu
import Meal
from rapidfuzz.fuzz import partial_ratio
class orderItems(SPXCafe):
    def __init__(self, order = None, mealId = None, mealPrice = None, quantity = None):
        super().__init__()
        self.SuperBot = Avatar("tenOutOfTenRestauraunt Bot")
        self.setOrder(order)
        # self.orderDb = orderDb.orderDb()
        self.totalPrice = 0
        self.setMealId(mealId)
        self.setMealPrice(mealPrice)
        self.setQuantity(quantity)
        # if self.existsDB():
        #     if not self.setOrderItems(self):
        #         print(f"order: {mealId}")

    def setOrderItems(self, orderId = None):
        '''Finds the orders from orderId'''
        dataList = []
        sql =None
        if orderId:
            sql = f'''SELECT orderItemId, orderId, mealId, quantity, mealPrice 
                FROM orderItems 
                WHERE orderId = '{orderId}'
                ORDER BY orderItemId
                '''
        else:
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
            self.setQuantity(self.quantity)
            self.setMealId(Meal.Meal(self.mealId))
            self.setMealPrice(self.mealPrice)
            self.totalPrice += int(self.getQuantity())*int(self.getMealPrice()) # gets total price of meal
            # print(f"total price: {self.totalPrice}")
            self.findMealName()
            dataList.append([self.getMealName(), self.getQuantity(), self.getMealPrice(), self.totalPrice])
        return dataList
        
    def existsDB(self, orderItemsId):
        retcode = False
        sql =None
        if orderItemsId:
            sql = f'''SELECT count(*) AS count FROM orderItems WHERE orderItemId = '{orderItemsId}' ''' #sql checks for amount of usernames in database
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
    @classmethod
    def getOrderItems(cls, order):
        ''''Get Meals for a course object or instance - example of aggregation'''
        orders = []
        if order:
            sql = f"SELECT orderItemId, orderId, mealPrice, quantity, mealId FROM orderItems WHERE orderId = {order.getOrderId()} ORDER BY orderItemId"
            # print(f"test all meals: {sql}")

            orderItemsData = SPXCafe().dbGetData(sql)

            for orderData in orderItemsData:
                # create a new instance
                newOrder = cls.__new__(cls)
                newOrder.setOrderItemId(orderData['orderItemId'])
                # order.setMealId(orderData['mealId'])
                newOrder.setOrder(order)
                newOrder.setMealPrice(orderData['mealPrice'])
                newOrder.setQuantity(orderData['quantity'])
                newOrder.setMeal(Meal.Meal(orderData['mealId']))
                orders.append(newOrder)
                # print(newOrder.getMeal(), newOrder.getMealPrice())
        return orders
     
    def display(self):
        print(f"| meal: {self.getMeal().getMealName()} | Quantity: {self.getQuantity()} | Price: ${self.getMealPrice()} |")
    def __str__(self):
        '''different variation to .display()'''
        return f"| meal: {self.getMeal().getMealName()} | Quantity: {self.getQuantity()} | Price: ${self.getMealPrice()} |"
            
    def isMatch(self, choice = None, match = None):
        '''To match and gain confidence in words''' # To do later
        confidence = partial_ratio(choice, match) # to edit
        # print(confidence, choice, match)
        if confidence >85:
            return True
        else:
            return False 
        
    def addOrderItem(self, mealId=None, quantity=None, mealPrice = None,orderId =None):
        '''adds individual orders to system'''
        sql = None 
        sql = f'''INSERT INTO orderItems (orderId, mealId, quantity, mealPrice) VALUES ('{orderId}','{mealId}','{quantity}','{mealPrice}')'''
        self.dbPutData(sql)


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
    def setOrder(self, orderId=None):
        if orderId:
            self.__orderId = orderId
        else:
            self.__orderId =None
    def getOrder(self):
        return self.__orderId
    # def setTotalPrice(self, totalPrice = None):
    #     self.__totalPrice = totalPrice
    # def getTotalPrice(self):
    #     return self.__totalPrice
    def setMealName(self, mealName=None):
        self.__mealName = mealName
    def getMealName(self):
        return self.__mealName
    def setMealPrice(self, mealPrice= None):
        self.__mealPrice = mealPrice
    def getMealPrice(self):
        return self.__mealPrice
    def setMeal(self, meal = None):
        if meal:
            self.__meal = meal
        else:
            self.__meal = []
    def getMeal(self):
        return self.__meal
def main():
    x=orderItems(1)
    x.findMealId('steak')
if __name__ == "__main__":
    main()