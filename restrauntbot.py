from Avatar2 import Avatar
from NLPdemo import NLPdemo
from SPXCafe2 import SPXCafe
from rapidfuzz.fuzz import partial_ratio
from rapidfuzz.process import extract
from rapidfuzz.utils import default_process
import menu
import restrauntCustomer
class tenOutOfTenRestaurant(SPXCafe):
    def __init__(self):
        '''Constructor method'''
        super().__init__()
        self.SuperWaiter = Avatar("tenOutOfTenRestaurant Bot") #
        self.SuperWaiter.introduce()
        # self.nlp = NLPdemo()
        self.callMenu = menu.Menu("TenOutOfTenRestauruant")
        self.match()
        self.orderMatch()
        self.menuChoiceRequest()
        self.nlp = NLPdemo()
        # if customer log in in database start this else try again so a while true loop
        print("------------------------ TenOutOfTenRestaurant ------------------------")
        if self.greetings():
            self.options() # if true send to customer options

# REQUESTS AND FUNCITION
    def getCustomerNewOrReturning(self):
        '''login or signup'''
        signedUp = False
        self.SuperWaiter.say("Please enter your username: ")
        userName = input("Please enter your username: ").lower() # for accuracy
        self.customer = restrauntCustomer.tenOutOfTenCustomer(userName=userName) # sets userName
        if self.customer.existsDBUserName(): # checks if username in database to prevent overlapping 
            signedUp = True
        else:
            firstName = self.SuperWaiter.say("Please enter your first name: ")
            firstName = input("Please enter your first name: ").lower() # asks first Name
            nameFirst = self.nlp.getNameByPartsOfSpeech(firstName)
            self.customer.setFirstName(nameFirst)                                # sets first Name
            self.SuperWaiter.say("Please enter your last name: ")       
            lastName = input("Please enter your last name: ").lower()   # asks last name .lower()
            nameLast = self.nlp.getNameByPartsOfSpeech(lastName)
            # print(nameLast.title())
            self.customer.setLastName(nameLast)                                  # sets last name
            self.customer.saveCustomer() 
            self.setCustomerId(self.customer.setCustomer())                                       # adds users to database (saves)            
            signedUp = True # ends signup loop
        self.SuperWaiter.say(f"Welcome to TenOutOfTenRestraunt by Cree gaming, {self.customer.getFirstName()} {self.customer.getLastName()}!") #Welcomes customer
        # print("Finished signup")
        return signedUp
    def greetings(self):
        '''login or signup options'''
        #inpNewOrReturning = self.SuperWaiter.listen("Please say Login if you want to Login, say sign up if you are new")
        while True:
            # self.SuperWaiter.say("Do you want to Order or 'Exit' ")
            enterOrExit = self.SuperWaiter.listen("Do you want to 'Order' or 'Exit' ").lower() # CHANGE TO WAITER SAYING THIS AND FUZZY
            order = ["order","stay","i would like to order"] # fuzzy logic
            leave = ["leave","bye","exit"]
            options = order+leave
            orderOrExit = self.getOptions(enterOrExit, options=options)
            if orderOrExit in order:
                return self.getCustomerNewOrReturning() # calls this
            elif orderOrExit in leave:
                return self.exit()        
            else:
                self.SuperWaiter.say("Please try again")

    def runMenu(self):
        '''displays the menu'''
        request = self.SuperWaiter.listen("Would you like to see the whole Menu, find a course or find a meal?", useSR=False) 
        # request = input("menu, course, find a meal: ")
        # ask for what they would like to see
        menuRQ = self.getOptions(request, self.menuOptions)
        running = True
        while running:
            self.callMenu.setMenuName("TenOutOfTen") # build fuzzy
            if menuRQ in self.menuRequest[0]:
                self.callMenu.display()
                running = False
            elif menuRQ in self.coursesRequest[0]:
                self.callMenu.displayCourses()
                # courseRequest = self.SuperWaiter.listen("Which course would you like to look at or would you like to go back to option?")
                # courseRequest = input("what course? ").lower() #to do fuzzy
                choice = self.courseFuzzy()
                if choice == "starter" or "entree":    # doesnt work if someone inputs starter so this is needed
            #             # find meal in course
                    self.callMenu.findCourse(choice)  
                elif choice == "dessert" or "finisher": # same as comment as before
                    self.callMenu.findCourse(choice)    
                elif choice  == "main":                 # doing this cbecuase same as others
                    self.callMenu.findCourse(choice)
                else:
                    self.SuperWaiter.say("Cannot find Course")
                running = False             # ask for what course or go back # to go back call a function that recalls the function
            elif menuRQ in self.findMealRequest[0]:
                    # searchMeal = self.SuperWaiter.listen("What meal do you want to search for?")
                searchMeal = input("what meal you want to find: ")
                self.findMeal(searchMeal, menuVer=True) #find meal function
                running =  False
                    # find all meals
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
        # make a match case senario using fuzzy logic where the waiter listens
        # to what the customer wants
    def courseFuzzy(self):
        self.callMenu.displayCourses()
        request = self.SuperWaiter.listen("Which course would you like to look at?")
        # courseRequest = input("what course? ").lower() #to do fuzzy
        self.courseList = ["main", "starter", "entree", "dessert", "finisher"]
        for course in self.courseList:
            choice = self.isMatch(request, course)
            if choice:
                return course

    def exit(self):
        '''Exit '''
        self.SuperWaiter.say("Thank you for coming to Ten Out of Ten Resturant by Cree gaming")
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
        print("|  Menu   |   Order History  |   Order   |   Exit   |")
        optionRun = True
        while optionRun == True:
            choice = self.getRequest()
            # print(choice)
            if choice in self.exitRequest["keywords"]:
                optionRun = False
                return self.exit()
            elif choice in self.historyRequest[0]:
                self.customer.displayOrderHistory()
            elif choice in self.menuRequest[0]:
                self.runMenu()
            elif choice in self.orderRequest[0]:
                optionRun = False
                return self.getFoodOrder()
        # option = self.SuperWaiter.listen("|Menu|       |Order History|       |Order|       |Exit|", useSR=False)
        # self.customer = restrauntCustomer.tenOutOfTenCustomer(userName='diamondf')
        # option = input("Menu, order history, order, exit: ").lower()
        # if option == "menu":
        #     self.runMenu()
        # if option == "history":
        #     self.customer.displayOrderHistory()
        # if option == "order":
        #     self.getFoodOrder()
        # if option == "Exit":
        #     self.exit()
        # choice = self.getOptions(option, self.mainOptions)
    def getFoodOrder(self):
        '''gets food orders'''
        totalItems = 0 
        ordering = True
        while ordering == True:
            # print("what do you want to order")
            foodOrder = self.SuperWaiter.listen("What do you want to order? ")
            orderFood = self.nlp.getMealByType(foodOrder)
            # # print(foodOrder)
            # orderFood = input("What do you want to order? ")
            self.meal = self.findMeal(orderFood)
            if self.meal == False:
                self.SuperWaiter.say("We failed to find your meal please try again")
                print("Failed to find Meal!")
            else:
                # quantity = self.SuperWaiter.listen("How many do you want? ") 
                # fuzzy logic will take a lot more code as whenever I 
                # say a number it either turns out to 
                # be a word or a number (I dont want to have to make something convert it for me
                quantity = input("What amount? ")
                self.customer.setBasket(self.findMealId(self.meal), quantity, self.meal)           # find the meal then add to basket # print(self.basket)
                self.customer.displayBasket()
                totalItems += int(quantity)
                # continueOrder = self.SuperWaiter.listen("Would you like to continue Ordering or go back options or abandon order: ") # TO DO FuZZY ADD KEY WORDS
                # continueOrder = input("Would you like to continue Ordering or go back options or abandon order: ")
                continueOrder = self.getOrderRequest()
                if continueOrder in self.checkoutRequest[0] and totalItems >=3:
                    self.customer.newOrder()
                    ordering = False
                    self.SuperWaiter.say("Thank you for ordering!")
                    self.options()
                elif continueOrder in self.abandonBasketRequest[0]:
                    self.SuperWaiter.say("Are you sure you want to Abandon Order? If so please type yes")
                    abandonConfirm = input("Are you sure you want to Abandon Order?: ").lower()
                    if abandonConfirm == "yes":
                        self.customer.delBasket()
                        ordering = False
                        self.options()
                elif continueOrder in self.optionsRequest[0] or self.checkoutRequest[0]:
                    ordering = False
        if continueOrder in self.checkoutRequest[0]:
            self.customer.checkOut()
        else:
            self.options()
        # if self.order == False:
        #     self.getRequest()
        # else:
        #     print("done")
    def findMealId(self, mealName=None):
        '''find Meals using there Names'''
        mealList = self.callMenu.findMeal(mealName)
        mealData = []
        if len(mealList) >1:
            for meals in mealList[0]:
                mealData.append(meals.getMealId())
                mealData.append(meals.getMealPrice())
                # mealData.append(meals.getMealName())
                print(mealData)
                return mealData
        else:
            for meals in mealList[0]:
                mealData.append(meals.getMealId())
                mealData.append(meals.getMealPrice())
                # mealData.append(meals.getMealName())
                return mealData

    def findMeal(self, meal = None, menuVer = False):
        '''finds meal using fuzzy logic'''
        if menuVer == True:
            meals = self.callMenu.findMeal(meal) # finds Meal
            if meals:
                for course in meals:
                    for meal in course:
                        meal.display() # displays Meal
            else:
                    print(f"{meal}' not found")
        else:
            self.meal = self.callMenu.findMeal(meal)
            # print(self.meal)
            self.mealList=[]
            if self.meal:
                for courses in self.meal:
                    for meals in courses:
                        print(f"We found {meals}")
                        self.mealList.append(meals.getMealName()) # gets meal stuff
                        # print(self.mealList)
            else:
                return False
            if len(self.meal) > 1: # for more than 1 get the first 1 
                # exactMeal = self.SuperBot.listen(f"Which {meal} do you want?")
                exactMeal = input(f"Which {meal} do you want? ")
                for food in self.mealList:
                    if self.isMatch(exactMeal, food):
                        self.SuperWaiter.say(f"You have chosen {food}") 
                        return food
                    else:
                        print(f"{food} did not match")
            else:
                for food in self.mealList:
                    return food

    def orderMatch(self):
        '''Key words for order'''
        self.abandonBasketRequest =      [["exit","leave","bye","abandon"],                            "abandon basket"]
        self.optionsRequest =   [["options"],                           "Go to options"]
        self.continueRequest =      [["continue", "order", "ordering"],     "continue ordering"]
        self.checkoutRequest =     [["finish", "check out","buy", "pay"],                           "checkout"]
        self.orderOptions = self.abandonBasketRequest[0] + self.optionsRequest[0] + self.continueRequest[0] + self.checkoutRequest[0]
    def getOrderRequest(self):
        '''gets customer request after ordering'''
        option = self.SuperWaiter.listen("Would you like to continue Ordering or go back options or abandon order?")
        choice = self.getOptions(option, self.orderOptions)
        if choice in self.abandonBasketRequest[0]:
            response = self.abandonBasketRequest[1]
        elif choice in self.optionsRequest[0]:
            response = self.optionsRequest[1]
        elif choice in self.continueRequest[0]:
            response = self.continueRequest[1]
        elif choice in self.checkoutRequest[0]:
            response = self.checkoutRequest[1]
        else:
            self.SuperWaiter.say(f"I am sorry, I don't understand you chocie. You said: '{option}'. Please try again.")
        self.SuperWaiter.say(f"Right, you chose to {response}")
        return choice
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
    def menuChoiceRequest(self):
        '''Key words for menu'''
        self.coursesRequest =      [["course","see the courses","see course","courses"],                            "see the courses"]
        self.menuRequest =   [["menu", "see the menu", "full menu", "whole menu"],                           "see the menu"]
        self.findMealRequest =      [["find a meal", "meal", " find meal"],     "find a meal"]
        # self.checkoutRequest =     [["finish", "check out","buy", "pay"],                           "checkout"]
        self.menuOptions = self.coursesRequest[0] + self.menuRequest[0] + self.findMealRequest[0] + self.checkoutRequest[0]
    def isMatch(self, choice=None, match = None):
        '''To match and gain confidence in words''' # To do later
        confidence = partial_ratio(choice, match) # to edit
        # print(confidence, choice, match)
        if confidence >85:
            return True
        else:
            return False 
    # getters/setters
    def setCustomerId(self, customerId=None):
        self.__customerId = customerId
    def getCustomerId(self):
        return self.__customerId 

    def basketTester(self):
        self.customer = restrauntCustomer.tenOutOfTenCustomer()
        self.customer.setCustomer('diamondf')
        self.customer.setBasket(self.findMealId("steak"), 3, "steak")           # find the meal then add to basket 
        print(self.customer.getBasket())
        self.customer.displayBasket()
        self.customer.checkOut()
def main():
    test = tenOutOfTenRestaurant()
    # test.basketTester()
    # test.basketTester()
    # print(test)
    '''TO TEST '''
    '''
    FOOD ORDER FUNC
    UPDATE IMAGE OF UML CLASS DIAGRAM
    DATA FLOW DIAGRAM DO
    DO SOME OTHER THINGS
    '''

if __name__=="__main__":
    main()        



