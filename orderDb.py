from SPXCafe2 import SPXCafe
from Avatar2 import Avatar
import orderItems
import restrauntCustomer
class orderDb(SPXCafe):
    def __init__(self, customerId = None, orderId = None, orderDate = None):
        '''Constructor '''
        super().__init__()
        self.SuperCustomer = Avatar("tenOutOfTenRestaurant Bot")
        self.setCustomerId(customerId)
        self.setOrderDates(orderDate)
        self.setOrderId(orderId)
        # self.orderItem = orderItems.orderItems()
        self.__orders = []
            # self.setOrder()
            # if not self.setOrder(self.__orderId):
            #     print(f"Course: Course Id <{self.getCourseId()}> is invalid")
        # print(self.getCustomerId())
        # customerID = customerId
        self.order = orderItems.orderItems()

    def setOrder(self, customerId = None):
        '''gets order ids and all orders made by customer'''
        sql =None
        if self.getCustomerId():
            sql = f'''SELECT orderId, orderDate, customerId 
            FROM Orders 
            WHERE customerId = '{self.getCustomerId()}'
            ORDER BY orderId
            '''
        else:
            sql = f'''SELECT orderId, orderDate, customerId 
            FROM Orders 
            WHERE customerId = '{customerId}'
            ORDER BY orderId
            ''' # print(sql)
        orderHSdata = self.dbGetData(sql)
            # print(orderHSdata)
        for orders in orderHSdata:
            self.orderId = orders['orderId']
            self.orderDate = orders['orderDate']
            # self.customerId = orders['customerId']
            self.setOrderId(self.orderId)
            self.setOrderDates(self.orderDate)
            # self.setOrder(orderItems.orderItems.getOrderItems(order=order))
            # self.setCustomerId(self.customerId)
                # print(self.getOrderId())
                # print(self.getOrderDates())           checks if they worked
                # print(self.getCustomerId())
            

    def existDbOrder(self, customerId=None):
        '''check if object already exists in datbase'''
        retcode = False
        sql =None
        if customerId:
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

    def display(self):
        '''Displays Order Data'''
        # print(f"orderId: {self.getOrderId()}| orderDate: {self.getOrderDates()} | customerId: {self.getCustomerId()}| mealId: {self.getMealId()}| quantity: {self.getQuantity()}| meal: {self.__mealName}| price: {self.__mealPrice}")
        # characters = f"| Order Date: {self.getOrderDates()} | Meal: {mealName} | Quantity: {self.getQuantity()} |  Price: {mealPrice} |"
        # print("-"*len(characters))
        # print(f"| Order Date: {self.getOrderDates()} | Meal: {mealName} | Quantity: {self.getQuantity()} |  Price: {mealPrice} |")
        # print("."*len(characters))
        allOrders= self.getAllOrder()
        # print(self)
        if allOrders:  
            for orderItem in allOrders:
                orderItem.display()
                print(f"{' '*46} Order Total: ${self.getOrderTotal()}")
                print("-"*len(orderItem))
        else: 
            print("You have had no orders with us!")

    def createOrder(self, basket = None):
        '''creates order'''
        sql = None
        # print(self.__orderDate, customerId)
        sql = f'''INSERT INTO Orders (orderDate, customerId) VALUES ('{self.getToday()}','{self.getCustomerId()}')
            '''
        self.setOrderId(self.dbPutData(sql))
        # print(self.setOrderId())
        # print(sql)
        if basket:
            for orders in basket:
                mealDataList = orders[0]
                # print(mealDataList)
                quantity = orders[1]
                # print(quantity)
                self.order.addOrderItem(mealId=mealDataList[0], quantity=quantity, mealPrice=mealDataList[1], orderId=self.getOrderId())
                print('FINISHED')


    # def orderFood(self):
    #     '''gets the order id by using order date'''
    #     sql = None
    #     sql = f'''SELECT orderId, orderDate, customerId 
    #         FROM Orders 
    #         WHERE orderDate = '{self.getToday()}'
    #         ORDER BY orderId '''
    #     orderData = self.dbGetData(sql)
    #     for data in orderData:
    #         self.orderId = data['orderId']
    #         self.setOrderId(self.orderId)
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
        if customerId:
            self.__customerId = customerId
        else:
            self.__customerId =None
    def getCustomerId(self):
        return self.__customerId
    def setQuantity(self, quantity = None):
        self.__quantity = quantity
    def getQuantity(self):
        return self.__quantity
    def setAllOrder(self, orders = None):
        if orders:
            self.__orders = orders
        else:
            self.__orders = []
    def getAllOrder(self):
        # print(self.__orders)
        return self.__orders
    def getOrderTotal(self):
        total = 0
        if self.__orders:
            for orderItems in self.__orders:
                total += orderItems.getMealPrice() * orderItems.getQuantity()
        return total

# factory method gets orders for user in init
    @classmethod
    def getOrders(cls, customerId):
        '''Class method: gets all order obejcts/ instances of customer orders - example of aggregation'''
        # if tenOutOfTenCustomer.getCustomerId():
        sql = f'''SELECT orderId, orderDate, customerId 
        FROM Orders 
        WHERE customerId = {customerId} 
        ORDER BY orderId, orderId'''
        # else:
        #     sql = f"SELECT orderId, orderDate, customerId FROM Orders WHERE customerId = {customerId} ORDER BY orderId"
        # print("yay")
        #print(f"get all courses: {sql}")
        ordersData = SPXCafe().dbGetData(sql)
        orders = []
        # print("works")
        for orderData in ordersData:
            # create a new instance
            order = cls.__new__(cls)
            order.setOrderId(orderData['orderId'])
            order.setOrderDates(orderData['orderDate'])
            order.setCustomerId(orderData['customerId'])
            orderItemsList = orderItems.orderItems.getOrderItems(order=order)
            order.setAllOrder(orderItemsList)
            # add course object to courses list
            # print(order.getOrderId(), order.getOrderDates(), order.getCustomerId())
            orders.append(order)
            # print(order.getOrderDates())
        # print(orders)
        return orders


def main():
    '''test harness'''
    orderHS= orderDb(customerId=1)
    orderHS.createOrder()
    # orderHS.orderHistory()
    # orderHs.display()
    
    # basker = [["streak", 3]]
    # orderHs.createOrder(customerId=1, basket=basker)
    # print("finish")
    # print(orderHs.getOrders(1))
if __name__ == "__main__":
    main()