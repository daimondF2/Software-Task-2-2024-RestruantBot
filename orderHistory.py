from SPXCafe2 import SPXCafe
from restrauntCustomer import tenOutOfTenCustomer
class orderHistor(SPXCafe):
    def __init__(self):
        super().__init__()
        self.customerInfo = tenOutOfTenCustomer()
        self.getToday()
        self.addOrders()



    def addOrders(self):
        # adds orders to order history
        pass
    def seeOrderHistory(self):
        sql =None
        if self.customerInfo.getCustomerId():
            sql = f'''SELECT orderId, orderDate, customerId FROM Orders WHERE customerId = '{self.customerInfo.getCustomerId()}' '''
            print(sql)
        orderHSdata = self.dbGetData(sql)
        print(orderHSdata)
    # You must be able to allow the customer to access their previous orders, including
    # Order number
    # Order Date
        pass

    def displayOrderHistory(self):
        pass
    
    # For Previous Orders

# The Meals/Dishes ordered and their prices (at that point in time)
# Total order value