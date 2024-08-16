from SPXCafe2 import SPXCafe
from Avatar2 import Avatar
import orderItems
class orderDb(SPXCafe):
    def __init__(self, customerId = None):
        '''Constructor '''
        super().__init__()
        self.SuperCustomer = Avatar("tenOutOfTenRestaurant Bot")
        self.getToday()
        self.totalPrice = 0
        self.setCustomerId(customerId)
        print("|---------------------- Past Orders ----------------------|")

    def setOrder(self):
        '''gets order ids and all orders made by customer'''
        sql =None
        if self.getCustomerId():
            sql = f'''SELECT orderId, orderDate, customerId 
            FROM Orders 
            WHERE customerId = '{self.getCustomerId()}'
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
                self.order = orderItems.orderItems(self.getOrderId())
                self.order.getOrderItems()
                # Call ORDER factory method to return a list of order objects/instances - pass self to it
        print(f"| Total price: {self.totalPrice} |") # displays total cost
        print("....................")
        
    def existDbOrder(self, customerId=None):
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

    def displayOrders(self):
        '''Displays Order Data'''
        # print(f"orderId: {self.getOrderId()}| orderDate: {self.getOrderDates()} | customerId: {self.getCustomerId()}| mealId: {self.getMealId()}| quantity: {self.getQuantity()}| meal: {self.__mealName}| price: {self.__mealPrice}")
        characters = f"| Order Date: {self.getOrderDates()} | Meal: {self.__mealName} | Quantity: {self.getQuantity()} |  Price: {self.__mealPrice} |"
        print("-"*len(characters))
        print(f"| Order Date: {self.getOrderDates()} | Meal: {self.__mealName} | Quantity: {self.getQuantity()} |  Price: {self.__mealPrice} |")
        print("."*len(characters))

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
    '''test harness'''
    orderHs= orderDb()
    orderHs.setOrder(customerId=1)
if __name__ == "__main__":
    main()