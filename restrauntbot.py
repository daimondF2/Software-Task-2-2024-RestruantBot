# View Menus
# Order food
# Your chat bot must have a Natural Conversation/Logic Flow and must be able to handle fuzzy input.
from Avatar2 import Avatar
from NLPdemo import NLPdemo
from SPXCafe2 import SPXCafe
from rapidfuzz.fuzz import partial_ratio
from rapidfuzz.process import extract
from rapidfuzz.utils import default_process
import menu
import Meal
from Course import Course
import restrauntCustomer
import Order
class tenOutOfTenRestaurant(SPXCafe):
    def __init__(self):
        '''Constructor method'''
        super().__init__()
        self.SuperWaiter = Avatar("tenOutOfTenRestaurant Bot") #
        self.SuperWaiter.introduce()
        self.nlp = NLPdemo()
        self.callMenu = menu.Menu()
        self.mealInfo = Meal.Meal()
        self.match()
        self.orderInfo = Order.orders()
        # if customer log in in database start this else try again so a while true loop
        print("------------------------ Cafe Name ------------------------")
        self.basket = []
        self.customer = restrauntCustomer.tenOutOfTenCustomer()
        self.greetings()
        # if self.customer.greetings():
        #     self.options()

    '''TO DO'''
    # order options then add basket check as an option
    # ADD OTHER things LIKE TIME TO DATABASE
    # do order and menu(find meal)
    # add fuzzy logic
        #self.options() # Need to setup options for the customer

# REQUESTS AND FUNCITION
    def greetings(self):
        '''login or signup options'''
        #inpNewOrReturning = self.SuperWaiter.listen("Please say Login if you want to Login, say sign up if you are new")
        while True:
            self.SuperWaiter.say("Do you want to Order or 'Exit' ")
            inpNewOrReturning = input("Do you want to 'Order' or 'Exit' ").lower() # CHANGE TO WAITER SAYING THIS AND FUZZY
            if inpNewOrReturning == "order":
                return self.customer.getCusotmerNewOrReturning() 
            elif inpNewOrReturning == "exit":
                return self.exit()        
            else:
                self.SuperWaiter.say("Please try again")

    def runMenu(self):
        '''displays the menu'''
        # request = self.SuperWaiter.listen("Would you like to see the whole Menu, find a course or find a meal?", useSR=False) 
        request = input("menu, course, find a meal")
        # ask for what they would like to see
        running = True
        while running:
            self.callMenu.setMenuName("TenOutOfTen") # build fuzzy
            if request == "menu":
                self.callMenu.display()
                running = False
            elif request == "course":
                self.callMenu.displayCourses()
                running = False
                # ask for what course or go back # to go back call a function that recalls the function
            elif request == "find a meal":
                # searchMeal = self.SuperWaiter.listen("What meal do you want to search for?")
                searchMeal = input("what meal you want to find: ")
                # find all meals
                meals = self.callMenu.findMeal(searchMeal)
                if meals:
                    for course in meals:
                        for meal in course:
                            meal.display()
                    running = False
                else:
                    print(f"{searchMeal}' not found")
                # find meal in a course
                # if self.mealInfo.isMatch(searchMeal):
                #     print('match')
                # else:
                #     print("not matched")
                # foundMeal = self.mealInfo.findMeal(searchMeal)
                # if foundMeal:
                #     foundMeal.display()      
            else:
                running =False
        self.options()
        # just to show the type of food that can be bought
        # if certain thing like see courses
        # ask for food 
        # make a match case senario using fuzzy logic where the waiter listens
        # to what the customer wants

        # For Menu
# They may see the dishes for one course only or for all courses
# You must include a price for each dish in that course

    def orderHistory(self):
        '''sends to orderhistory then back to options'''
        self.customer.history()
        self.options()

    def exit(self):
        '''Exit '''
        print("Thank you for coming to our thing")

    def isMatch(self, request= None):
        '''To match and gain confidence in words''' # To do later
        confidence = partial_ratio(request, self.match()) # to edit
        # print(courseName, self.getCourseName(), confidence)
        if confidence >80:
            return True
        else:
            return False
        
    def match(self): # key words and stuff
        '''Key words for requests'''
        self.exitRequest =      {
                "keywords":      ["exit","leave","bye"],
                "response":      "leave us now"
        }
        self.historyRequest =   {
                "keywords":     ["history", "previous"],
                "response":     "see your previous orders"
        }
        # self.exitRequest =      [["exit","leave","bye"],                            "leave us now"]
        self.historyRequest =   [["history", "previous"],                           "see your previous orders"]
        self.menuRequest =      [["menu", "course", "meal","choice","options"],     "see the menu"]
        self.orderRequest =     [["order", "buy","food"],                           "order some food"]
        self.mainOptions = self.exitRequest["keywords"] + self.historyRequest[0] + self.menuRequest[0] + self.orderRequest[0]

        # ORDER WORDS



    def options(self):
        '''sends customer to chosen area'''
        print("----------------------- Options ------------------------")
        # choice = self.getRequest()
        # print(choice)

        # if choice in self.exitRequest["keywords"]:
        #     return self.exit()
        #     running = False
        # elif choice in self.historyRequest[0]:
        #     return self.orderHistory()
        # elif choice in self.menuRequest[0]:
        #     return self.runMenu()
        # elif choice in self.orderRequest[0]:
        #     return self.getFoodOrder()
        option = self.SuperWaiter.listen("|Menu|       |Order History|       |Order|       |Exit|", useSR=False)
        option = input("Menu, order history, order, exit: ").lower()
        if option == "menu":
            self.runMenu()
        if option == "history":
            self.orderHistory()
        if option == "order":
            self.getFoodOrder()
        if option == "Exit":
            self.exit()
        choice = self.getOptions(option, self.mainOptions)

############ Getters/ setters ##############
    def getFoodOrder(self):
        '''gets food orders'''
        totalItems = 0 
        ordering = True
        while ordering == True:
            foodOrder = self.SuperWaiter.listen("What do you want to order? ")  # TO DO FUZZY ADD KEY WORDS
            meal = self.orderInfo.findOrder(foodOrder)
            quantity = self.SuperWaiter.listen("How many do you want? ")
            self.basket[foodOrder] = quantity           # find the meal then add to basket
            totalItems += quantity
            continueOrder = self.SuperWaiter.listen("Would you like to continue Ordering or go back options: ") # TO DO FuZZY ADD KEY WORDS
            if continueOrder == "finish":
                ordering = False
        if self.basket:
            self.customer.newOrder()

        # if self.order == False:
        #     self.getRequest()
        # else:
        #     print("done")

    def getRequest(self):       # gets request Options
        '''gets customer Request'''
        option = self.SuperWaiter.listen("What would you like to do?", useSR=False)
        choice = self.getOptions(option, self.mainOptions)
        if choice in self.exitRequest["keywords"]:
            response = self.exitRequest["response"]
        elif choice in self.historyRequest[0]:
            response = self.historyRequest[1]
        elif choice in self.menuRequest[0]:
            response = self.menuRequest[1]
        elif choice in self.orderRequest[0]:
            response = self.orderRequest[1]
        else:
            self.SuperWaiter.say(f"I am sorry, I don't understand your choice. You said: '{option}. Please try again.")
        self.SuperWaiter.say(f"Right, You chose to {response}.")
        return choice
          
    def getOptions(self, choice=None, options=None):    
        '''Chooose from a list of options'''
        matches = []
        maxConfidence= 0
        while len(matches)==0:
            if not choice:
                choice = self.SuperWaiter.listen().strip().lower()
                if not choice:
                    break
            
            results = extract(choice, options, scorer=partial_ratio, processor=default_process)
            for result in results:
                (match, confidence, index) = result
                # print(f"Checking: {result}")
                if confidence > maxConfidence:
                    maxConfidence = confidence
                    matches = [match]
                elif confidence == maxConfidence:
                    matches.append(match)
            # print(f" You have matched: {','.join(matches)} with confidence level {maxConfidence}% {len(matches)}")
            # if len(matches)>1:
            #     print("Sorry, you need to choose only one! Try again")
            #     options = matches
            #     matches = []
            #     maxConfidence = 0
        return matches[0] if len(matches)>0 else []

def main():
    test = tenOutOfTenRestaurant()
    test.runMenu()

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


