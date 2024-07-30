#You are to create a Restaurant Online Take Away Ordering Service 
#Chat Bot named by the type of food your restaurant serves
# Interact with the Customer to
# View order history
# View Menus
# Order food
# Your chat bot must have a Natural Conversation/Logic Flow and must be able to handle fuzzy input.
from Avatar2 import Avatar
from NLPdemo import NLPdemo
from SPXCafe2 import SPXCafe
from rapidfuzz import fuzz, process
from rapidfuzz.fuzz import partial_ratio
from menu import Menu
import Meal
from Course import Course
from restrauntCustomer import tenOutOfTenCustomer

class tenOutOfTenRestraunt(SPXCafe):
    def __init__(self):
        '''Constructor method'''
        self.SuperWaiter = Avatar("SuperBot") #
        self.nlp = NLPdemo()
        self.cafe= SPXCafe()
        self.callMenu = Menu()
        # if customer log in in database start this else try again so a while true loop
        print("------------------------ Cafe Name ------------------------")
        self.customer = tenOutOfTenCustomer()
        if self.customer.LoginOrSignUpOrExit(): #if true get request else move to signup
            self.getRequest()


    '''TO DO'''
    # COMPLETE LOGIN AND FINISH ACCESS STUFF
    # CHECK DATBASE FOR LOGIN
    # add database access
    # CREATE ORDER HISTORY IN DATBASE AND FILE
    # ADD OPTIONS
    # ADD OTHER things LIKE TIME TO DATABASE
    # add fuzzy logic
        #self.options() # Need to setup options for the customer
    def menu(self):
        '''displays the menu'''
        # might add menu find here but menu is mostly 
        # just to show the type of food that can be bought
        self.callMenu.setMenuName("TenOutOfTen") 
        # ask for what they would like to see
        self.callMenu.displayCourses()
        # if whole menu 
        self.callMenu.display()
        # if certain thing like see courses
        # ask for food 
        # make a match case senario using fuzzy logic where the waiter listens
        # to what the customer wants
        
    def exit(self):
        print("Thank you for coming to our thing")

    # Getters/ setters

    def getRequest(self):
        self.SuperWaiter.say("What would you like to do?")
        # option = self.SuperWaiter.listen("|Menu|       |Order History|       |Order|       |Exit|", useSR=False)
        option = input("Menu, order history, order, exit").lower()
        if option == "menu":
            self.menu()
        if option == "order history":
            self.orderHistory()
        if option == "Order":
            self.order()
        if option == "Exit":
            self.exit()
        # keywords = 

# ARCHIVE OF CODE THAT COULD WORK
    # def addUser(self):
    #     sql = None
        # if self.getUserName():
        #     sql = f"INSERT INTO Customers (userName) VALUES ({self.getUserName()})"
        # if self.getFirstName():
        #     sql = f"INSERT INTO Customers (firstName) VALUES ({self.getFirstName()})"
        # if self.getLastName():
        #     sql = f"INSERT INTO Customers (lastName) VALUES ({self.getLastName()})"
        # sql = f'''INSERT INTO customers (userName, firstName, lastName) VALUES
        #         ('{self.getUserName()}','{self.getFirstName()}','{self.getLastName()}')'''
        # self.dbPutData(sql) 
def main():
    test = tenOutOfTenRestraunt()

if __name__=="__main__":
    main()

#You must be able to store orders for a particular customer username 
#– using order numbers to differentiate between each order the customer made

# You must be able to store orders for a particular customer username – using order numbers to differentiate between each order the customer made

# Customer Actions

# The main things that the customer is allowed to do are:
# Order food
# View previous orders
# See the menu
# Exit the system

# For Previous Orders
# You must be able to allow the customer to access their previous orders, including
# Order number
# Order Date
# The Meals/Dishes ordered and their prices (at that point in time)
# Total order value

# For Menu
# You must be able to allow the customer to request a description of the menus for 3 different courses – e.g. starter, main and dessert
# They may see the dishes for one course only or for all courses
# You must include a price for each dish in that course

# For Ordering Food
# You must be able to allow the customer to order food from each of the courses

# Each order must have a minimum number of 3 dishes in order to proceed to checkout
# If less than 3 dishes ordered, then the order cannot be saved
# They may leave ordering at any time and abandon the order – please confirm they really want to do this.

# If 3 or more dishes ordered,
# They may continue ordering or finish ordering
# During the order process, the customer should be able to request to access the menu again or abandon the order.
# On completion of ordering/checkout,
# you must summarise the order when they have completed ordering
# What dishes they ordered and the price
# Total order cost
# and then ask them for confirmation to proceed to store order
# Once confirmed to go ahead to complete the order, the order is to be saved to the customer account
# Order number
# Dishes and Prices
# Total cost
# For Exit
# Thank the customer by name and wish them well and ask them to come back again another time in a polite way.