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
from rapidfuzz import fuzz, process
from rapidfuzz.fuzz import partial_ratio
class tenOutOfTenRestraunt():
    def __init__(self):
        self.SuperWaiter = Avatar("SuperBot")
        self.nlp = NLPdemo()
        # if customer log in in database start this else try again so a while true loop
        self.greetings()
        self.getPersonName
        self.getFirstName
    # Customer Greeting
    # You must be able to identify each customer by asking their username (typed in for accuracy).
    # If they are existing Customers then, by name,
    # Welcome them back
    # Otherwise
    # Welcome them to the service
    # Ask for them to enter their first and lastnames separately

    '''TO DO'''
    # COMPLETE LOGIN AND SIGNUP STUFF
    # CHECK DATBASE FOR LOGIN AND SIGNUP
    # CREATE ORDER HISTORY IN DATBASE AND FILE
    # ADD OPTIONS
    # ADD OTHER OPTIONS LIKE TIME TO DATABASE


    def greetings(self):
        self.introduction()
        self.LoginOrSignUpOrExit()

    def introduction(self):
        self.SuperWaiter.say("Welcome to Ten out of ten restraunt")
        self.SuperWaiter.say("Welcome to bot I am Super Helpful ultra bot")

    def LoginOrSignUpOrExit(self):
        #inpNewOrReturning = self.SuperWaiter.listen("Please say Login if you want to Login, say sign up if you are new")
        while True:
            inpNewOrReturning = input("Do you want to 'Login' or 'Signup' or 'Exit' ").lower()
            if inpNewOrReturning == "login":
                return self.login()
            elif inpNewOrReturning == "signup":
                return self.signUp()
            elif inpNewOrReturning == "exit":
                return self.exit()
            else:
                self.SuperWaiter.say("Please try again")
            
    def login(self):
        print("login")
        self.firstname = input("What is your first name? ")
        self.lastName
        self.exit()
        # What is First name? - 
        # what is last name? 
        # check in database
        # if not in data base
        # ask try again
        # if forgot ask if they would like to sign up
        # redirect
        # add name to datbase
        # if name in list
        # f" Welcome {getCustomerName()} {getCustomerLastName()}
        pass
    def signUp(self):
        print("signUp")
        self.getUserName()
        # ask name 
        # ask last name
        # add to database
        # welcome again and give options to see menu
    
    def getFirstName(self):
        pass
    def getLastName(self):
        pass
    
    def getCustomer(self):
        pass
    def getCustomerName(self):
        pass
    def getCustomerLastName(self):
        pass
    def getUserName(self):
        #ask for userName
        #if username in database:
        # login
        #if not in database
        # ask try again or forgot
        #If forgot
        # ask first name
        # ask last name
        #if in databse login
        # else
        #ask try again or ask sign up
        pass
    def exit(self):
        print("Thank you for coming to our thing")
        
def main():
    pass
if __name__=="__main__":
    main()
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