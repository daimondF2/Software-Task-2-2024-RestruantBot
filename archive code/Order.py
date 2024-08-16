from SPXCafe2 import SPXCafe
from Avatar2 import Avatar
import restrauntCustomer
import menu
from rapidfuzz.fuzz import partial_ratio
class orders(SPXCafe):
    def __init__(self, orderId=None, orderDate=None, customer=None):
        '''constructor class'''
        super().__init__()
        self.SuperBot = Avatar("tenOutOfTenRestaurant Bot")
        self.customerInfo = restrauntCustomer.tenOutOfTenCustomer()
        self.setCustomer(customer)
        self.__orderDate = self.getToday()
        self.menu = menu.Menu()

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

    def orderFood(self):
        '''gets the order id by using order date'''
        sql = None
        sql = f'''SELECT orderId, orderDate, customerId 
            FROM Orders 
            WHERE orderDate = '{self.__orderDate}'
            ORDER BY orderId '''
        orderData = self.dbGetData(sql)
        for data in orderData:
            self.orderId = data['orderId']
            self.setOrderId(self.orderId)

    def addOrderItem(self, mealId=None, quantity=None, mealPrice = None):
        '''adds individual orders to system'''
        sql = None
        sql = f'''INSERT INTO orderItems (orderId, mealId, quantity, mealPrice) VALUES ('{self.getOrderId()}','{mealId}','{quantity}','{mealPrice}')'''
        self.dbPutData(sql)

    def createOrder(self, customerId=None, basket = None):
        '''creates order'''
        sql = None
        print(self.__orderDate, customerId)
        sql = f'''INSERT INTO Orders (orderDate, customerId) VALUES ('{self.__orderDate}','{customerId}')
            '''
        self.dbPutData(sql)
        print(sql)
        self.orderFood()
        if basket:
            for orders in basket:
                self.findMealByName(mealName=orders[0])
                quantity = orders[1]
                self.addOrderItem(mealId=self.getMealId(), quantity=quantity, mealPrice=self.getMealPrice())
                print('FINISHED')

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

    def deleteOrder(self):
        rq = None
        sql == None
        if rq == "Abandon":
            # abandon order
            sql = ''''''
        '''Deletes an instance of a course from the database only if there are no children meals'''
        if rq==False:
            sql = f"DELETE FROM orderItems WHERE orderId={self.getOrderId()}"
            self.dbChangeData(sql)

    def exit(self):
        print("thank you for coming to our thing")
# For Exit
# Thank the customer by name and wish them well and ask them to come back again another time in a polite way.

######## getters/setters ##############
    def setOrderId(self, orderId):
        self.__orderId = orderId
    def getOrderId(self):
        return self.__orderId
    def setCustomer(self, customer=None):
        self.__customer= customer
    def getCustomer(self):
        return self.__cusotmer
    def setMealName(self, mealName=None):
        self.__mealName = mealName
    def getMealName(self):
        return self.__mealName
    def setMealId(self, mealId=None):
        self.__mealId = mealId
    def getMealId(self):
        return self.__mealId
    def setMealPrice(self, mealPrice=None):
        self.__mealPrice = mealPrice
    def getMealPrice(self):
        return self.__mealPrice

def main():
    '''test Harness'''
    o = orders()
    yourmum = input("what the fk do you want to get: ")
    x= o.findOrder(meal=yourmum)
    print(x)
    # b = [['steak',2],['Tenoutoften Specialty',2]]
    # o.checkOut(basket=b)
    # o.findMealByName("steak")
    
if __name__=="__main__":
    main()

# def getOrders(self):
#     sql = None
#     if self.customerInfo.getCustomerId():
#         sql = f'''SELECT orderId, orderItemId, customerId 
#         FROM orderItems
#         WHERE customerId = '{self.customerInfo.getCustomerId()}'
#         ORDER BY orderId
#         '''
#         self.dbGetData(sql)
