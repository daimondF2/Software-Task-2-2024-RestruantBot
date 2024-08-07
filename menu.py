from Course import Course
from Meal import Meal
from SPXCafe2 import SPXCafe

class Menu(SPXCafe):

    def __init__(self,menuName=None):
        '''constructor method for the menu'''

        super().__init__()
        self.setMenuName(menuName)
        #set the menu to datbase values
        self.setMenu()

    #getters and setters for menu ----------------------

    def setMenu(self):
        '''setup menu from dabase'''

        #add course aggregation for this menu - i.e a list of courses
        self.setCourses(Course.getCourses(self))

    def setMenuName(self, menuName=None):
        if menuName:
            self.__menuName = menuName
        else:
            self.__menuName = "The idiot"
    
    def setCourses(self,courses=None):
        '''set courses aggregation to list of Courses or empty list'''
        if courses:
            self.__courses = courses
        else:
            self.__courses = []
    
    def getMenuName(self):
        '''return the menu name'''
        return f"{self.__menuName} Menu"
    
    def getCourses(self):
        '''return a list of courses aavailable for this menu'''
        return self.__courses
    
    # ------output related methods -----------

    def __str__(self):
        '''returns a string for the menu object for printing this object'''
        return f"{self.getMenuName()} Menu"
    
    def display(self):
        '''disp[lau this menu instanvre more formally]'''
        print(f"{'-'*25} {self.getMenuName()} {'-'*25}\n")
        if self.getCourses():
            for course in self.getCourses():
                course.display()
        

    def displayCourses(self):
        '''Display all the courses  uin a comma - seperet string'''
        print(f"Course List: ",end="")
        courseNames=[]
        for course in self.getCourses():
            courseNames.append(course.getCourseName().title())
        print(". ".join(courseNames))
        print()

    #author\: methods for menu and aggregation courses
    def findMeal(self, searchMeal=None):
        allmeals = []
        # course.searchcours(searchcourse)
        # course. searchmeal
        if searchMeal:
            for course in self.getCourses(): # for all courses (3) meal = course.findMeal(searchMeal)
                meals = course.findMeal(searchMeal)
                if meals:
                    allmeals.append(meals)
                    # self.setMealList(allmeals)
                    # print(self.getMealList())

        return allmeals
    
    def findCourse(self, searchCourse=None):
        courses = []
        if searchCourse:
            for course in self.getCourses():
                courses.append(course.findCourse(searchCourse))
        return courses

    def setMealList(self, meals):
        self.__MealList = meals
    
    def getMealList(self):
        return self.__MealList

def main():
    '''test harness sure all methods work'''
    menu = Menu("The idiot")
    menu.display()

    menu.displayCourses()

    # Find a meal - using fuzzy logic - finds partial
    searchMeal = input("What meal do you want? ")
    meals = menu.findMeal(searchMeal)
    if meals:
        print(f"we have ofund the follow meals:{meals}")
        for meal in meals:
            for thing in meal:
                thing.display()
    else:
        print(f"{searchMeal}' not found")
    # searchCourse = input("what course do you want? ")
    # courses = menu.findMeal(searchCourse)
    # if courses:
    #     print(" we have found foillowing courses")
    #     for course in courses:
    #         print("we found course")
    #         course.display()
    # else:
    #     print(f"'{searchCourse}' not ofund")
if __name__=="__main__":
    main()