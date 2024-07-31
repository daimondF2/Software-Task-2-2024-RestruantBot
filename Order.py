from SPXCafe2 import SPXCafe
from Avatar2 import Avatar
class orders(SPXCafe):
    def __init__(self):
        super().__init__
        self.SuperBot = Avatar("tenOutOfTenRestaurant Bot")
    def databaseAccess(self):
        pass
    
    def orderFood(self):
        self.
        # For Ordering Food
# You must be able to allow the customer to order food from each of the courses

# Each order must have a minimum number of 3 dishes in order to proceed to checkout
# If less than 3 dishes ordered, then the order cannot be saved
# They may leave ordering at any time and abandon the order – please confirm they really want to do this.
        pass
# If 3 or more dishes ordered,
# They may continue ordering or finish ordering
# During the order process, the customer should be able to request to access the menu again or abandon the order.
    def getOrders(self):
        pass

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

# onced finish buy add to to orderhistory
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
        else:
            print(f"Cannot delete Course {self.getCourseId()}-{self.getCourseName().title()} -  Meals attached")

    def setOrderId(self, orderId):
        self.__orderId = orderId

    def getOrderId(self):
        return self.__orderId

    def exit(self):
        print("thank you for coming to our thing")
# For Exit
# Thank the customer by name and wish them well and ask them to come back again another time in a polite way.