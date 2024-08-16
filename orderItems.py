from SPXCafe2 import SPXCafe
from Avatar2 import Avatar
import restrauntCustomer
import menu
import orderDb
from rapidfuzz.fuzz import partial_ratio
class orderItems(SPXCafe):
    def __init__(self, orderId = None):
        super().__init__()
        self.SuperBot = Avatar("tenOutOfTenRestauraunt Bot")
        self.setOrderId(orderId)
        self.menu = menu.Menu()

    def getOrderItems(self, orderId = None):
        '''Finds the orders from orderId'''
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
            self.setMealId(self.mealId)
            self.setMealPrice(self.mealPrice)
            self.totalPrice += int(self.getQuantity())*int(self.getMealPrice()) # gets total price of meal
            # print(f"total price: {self.totalPrice}")
            self.findMealName()

    def findMealName(self):
        '''gets the mealName form mealId'''
        sql = None
        sql = f'''SELECT mealId, mealName, mealPrice, courseId 
            FROM meals 
            WHERE mealId = '{self.getMealId()}'
            ORDER BY mealId
            '''
        mealData = self.dbGetData(sql)
        for meals in mealData:
            self.setMealName(meals['mealName'])
            self.displayOrderHistory()


    def findOrder(self, meal = None):
        '''finds Order using fuzzy logic'''
        self.meal =  self.menu.findMeal(meal)
        # print(self.meal)
        self.mealList=[]
        if self.meal:
            for courses in self.meal:
                for meals in courses:
                    print(f"We found {meals}")
                    self.mealList.append(meals.getMealName())
                    # print(self.mealList)
        else:
            return False
        if len(self.meal) > 1:
            # exactMeal = self.SuperBot.listen(f"Which {meal} do you want?")
            exactMeal = input(f"Which {meal} do you want? ")
            for food in self.mealList:
                if self.isMatch(exactMeal, food):
                    self.SuperBot.say(f"You have chosen {food}")
                    return food
                else:
                    print(f"{food} is did not match")
        else:
            for food in self.mealList:
                return food
            
    def isMatch(self, choice = None, match = None):
        '''To match and gain confidence in words''' # To do later
        confidence = partial_ratio(choice, match) # to edit
        # print(confidence, choice, match)
        if confidence >85:
            return True
        else:
            return False 
        
    def addOrderItem(self, mealId=None, quantity=None, mealPrice = None):
        '''adds individual orders to system'''
        sql = None
        sql = f'''INSERT INTO orderItems (orderId, mealId, quantity, mealPrice) VALUES ('{self.getOrderId()}','{mealId}','{quantity}','{mealPrice}')'''
        self.dbPutData(sql)

    def findMealByName(self, mealName=None):
        '''find Meals using there Names'''
        sql = None
        if mealName:
            sql = f"SELECT mealId, mealName, mealPrice, courseId FROM meals WHERE mealName = '{mealName}'"
            mealData = self.dbGetData(sql)
            for meals in mealData:
                self.setMealId(meals['mealId'])
                self.setMealPrice(meals['mealPrice'])

    def displayBasket(self, basket=None):
        '''Displays basket'''
        totalOrderPrice = 0
        if basket:
            print("|--------------------- Order ---------------------|")
            for orderItems in basket:
                totalPrice = 0
                self.findMealByName(orderItems[0])
                totalPrice += int(self.getMealPrice())*int(orderItems[1])
                totalOrderPrice +=totalPrice
                print(f"Meal: {orderItems[0]} | Quantity: {orderItems[1]} | Total Price: {totalPrice}")
            print(f"| Total Order Price: {totalOrderPrice} |")

    def checkOut(self, basket=None):
        '''checkOut system'''
        customerOrder = basket
        self.displayBasket(basket=customerOrder)
        orderConfirm = self.SuperBot.listen("Would you liek to confirm Order? ")
        if orderConfirm == "yes":
            self.createOrder(basket=customerOrder)




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
    def setTotalPrice(self, totalPrice = None):
        self.__totalPrice = totalPrice
    def getTotalPrice(self):
        return self.__totalPrice
    def setMealName(self, mealName=None):
        self.__mealName = mealName
    def getMealName(self):
        return self.__mealName
    def setMealPrice(self, mealPrice= None):
        self.__mealPrice = mealPrice
    def getMealPrice(self):
        return self.__mealPrice