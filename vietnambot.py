#You are to create a Restaurant Online Take Away Ordering Service 
#Chat Bot named by the type of food your restaurant serves
# Vietnamese Food – call yours VietnamBot
# You need to Identify a Customer - new or existing
# Interact with the Customer to
# View order history
# View Menus
# Order food
# Your chat bot must have a Natural Conversation/Logic Flow and must be able to handle fuzzy input.
from Avatar2 import Avatar
from NLPdemo import NLPdemo
from SPXCafe2 import SPXCafe
class tenOutOfTenRestraunt():
    def __init__(self):
        self.vietnamesePerson = Avatar("VietnamBot")
        #   
        # Introduction
        # On startup, you application must identify itself by name and welcome the customer in a polite way
        
        # if customer log in in database start this else try again so a while true loop
        self.vietnamesePerson.say("Welcome to bot bot")
        self.greetings()
        self.welcomePerson
        self.getPersonName
        self.getFirstName
    # Customer Greeting
    # You must be able to identify each customer by asking their username (typed in for accuracy).
    # If they are existing Customers then, by name,
    # Welcome them back
    # Otherwise
    # Welcome them to the service
    # Ask for them to enter their first and lastnames separately
    def introduction(self):
        self.vietnamesePerson.say("Welcome to Ten out of ten restraunt")
        self.vietnamesePerson.say("Please Login or Sign up")
    def greetings(self):
        self.vietnamesePerson.say("what up my - how are you")
        while True:
            self.vietnamesePerson.listen("")
            self.firstname
            self.lastName
        self.exit()
        # What is First name? - 
        # what is last name? 
        # check in database
        # if not in data base
        # add name to datbase
        # if name in list
        # f" Welcome {getCustomerName()} {getCustomerLastName()}
        pass
    def getCustomer(self):
        pass
    def getCustomerName(self):
        pass
    def getCustomerLastName(self):
        pass
    def exit(self):
        print("Thank you for coming to our thing")
        

# Customer Greeting
#You must be able to identify each customer by asking their username (typed in for accuracy).
#If they are existing Customers then, by name,
#Welcome them back
#Otherwise
#Welcome them to the service
#Ask for them to enter their first and lastnames separately

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