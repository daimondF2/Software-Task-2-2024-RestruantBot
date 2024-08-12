from SPXCafe2 import SPXCafe
from Avatar2 import Avatar
import restrauntCustomer
import menu
class orders(SPXCafe):
    def __init__(self, orderId=None, orderDate=None, customer=None):
        '''constructor class'''
        super().__init__()
        self.SuperBot = Avatar("tenOutOfTenRestaurant Bot")
        self.customerInfo = restrauntCustomer.tenOutOfTenCustomer()
        self.setCustomer(customer)
        self.__orderDate = self.getToday()
        self.menu = menu.Menu()

    def askOrder(self):
        # asks for stuff right for fuzzy
        pass
    def findOrder(self, meal = None):
        self.meal =  self.menu.findMeal(meal)
        for courses in self.meal:
            for meals in courses:
                print(meals)



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
        # For Ordering Food
# You must be able to allow the customer to order food from each of the courses

# Each order must have a minimum number of 3 dishes in order to proceed to checkout
# If less than 3 dishes ordered, then the order cannot be saved
# They may leave ordering at any time and abandon the order – please confirm they really want to do this.
# If 3 or more dishes ordered,
# They may continue ordering or finish ordering
# During the order process, the customer should be able to request to access the menu again or abandon the order.

    def createOrder(self, customerId=None):
        '''creates order ids'''
        sql = None
        print(self.__orderDate, customerId)
        sql = f'''INSERT INTO Orders (orderDate, customerId) VALUES ('{self.__orderDate}','{customerId}')
            '''
        print(sql)
        self.dbPutData(sql)

    def checkOut(self):
        pass
# On completion of ordering/checkout,
# you must summarise the order when they have completed ordering
# What dishes they ordered and the price
# Total order cost
# and then ask them for confirmation to proceed to store order
# Once confirmed to go ahead to complete the order, the order is to be saved to the customer account
# Order number
# Dishes and Prices
# Total cost

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
    # def getOrders(self):
    #     sql = None
    #     if self.customerInfo.getCustomerId():
    #         sql = f'''SELECT orderId, orderItemId, customerId 
    #         FROM orderItems
    #         WHERE customerId = '{self.customerInfo.getCustomerId()}'
    #         ORDER BY orderId
    #         '''
    #         self.dbGetData(sql)

    def setOrder(self):
        sql = None
        sql = ''''''

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





# Make new Order Id and customer Id
#ask for meal and orderItem
# find meal then add to orderItem and give it orderId
#repeat

def main():
    o = orders()
    yourmum = input("what the fk do you want to get: ")
    o.findOrder(meal=yourmum)
    
if __name__=="__main__":
    main()