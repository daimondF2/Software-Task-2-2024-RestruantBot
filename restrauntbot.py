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
        super().__init__()
        self.SuperWaiter = Avatar("tenOutOfTenRestraunt Bot") #
        self.SuperWaiter.introduce()
        self.nlp = NLPdemo()
        self.callMenu = Menu()
        # if customer log in in database start this else try again so a while true loop
        print("------------------------ Cafe Name ------------------------")
        self.customer = tenOutOfTenCustomer()
        if self.customer.getCusotmerNewOrReturning(): #if true get request else move to signup
            self.getRequest()


    '''TO DO'''
    # add database access
    # CREATE ORDER HISTORY IN DATBASE AND FILE
    # ADD OPTIONS
    # ADD OTHER things LIKE TIME TO DATABASE
    # add fuzzy logic
        #self.options() # Need to setup options for the customer
    def menu(self):
        '''displays the menu'''
        request = self.SuperWaiter.listen("Would you like to see the whole Menu, find a course or find a meal?", useSR=False) 
        # ask for what they would like to see
        self.callMenu.setMenuName("TenOutOfTen") 
        if request == "menu":
            self.callMenu.display()
        elif request == "course":
            self.callMenu.displayCourses()
            # ask for what course
        elif request == "find a meal":
            self.callMenu.findMeal()
        else:
            self.getRequest()
        # just to show the type of food that can be bought
        # if whole menu 
        # if certain thing like see courses
        # ask for food 
        # make a match case senario using fuzzy logic where the waiter listens
        # to what the customer wants

        # For Menu
# You must be able to allow the customer to request a description of the menus for 3 different courses – e.g. starter, main and dessert
# They may see the dishes for one course only or for all courses
# You must include a price for each dish in that course


    def getFoodOrder(self):
        self.Order

    def orderHistory(self):
        self.order
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
            self.getFoodOrder()
        if option == "Exit":
            self.exit()
        # keywords = 

    def isMatch(self, courseName= None):
        '''To edit fuzzy''' # To do later
        # confidence = partial_ratio(courseName.lower(), self.getCourseName().lower()) # to edit
        # print(courseName, self.getCourseName(), confidence)
        if confidence >80:
            return True
        else:
            return False
def main():
    test = tenOutOfTenRestraunt()

if __name__=="__main__":
    main()        

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


#You must be able to store orders for a particular customer username 
#– using order numbers to differentiate between each order the customer made
# You must be able to store orders for a particular customer username – using order numbers to differentiate between each order the customer made
# Customer Actions

# The main things that the customer is allowed to do are:
# Order food
# View previous orders
# See the menu
# Exit the system


