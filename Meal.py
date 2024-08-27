from SPXCafe2 import SPXCafe
import Course
from rapidfuzz.fuzz import QRatio, partial_ratio, ratio, WRatio

class Meal(SPXCafe):

    def __init__(self,mealId=None, mealName=None, mealPrice=None, courseId=None,course=None):
        super().__init__()
        self.setMealId(mealId)
        self.setMealName(mealName)
        self.setMealPrice(mealPrice)
        self.setCourseId(courseId)
        self.setCourse(course)
        # This checks if Meal already exists... if so, just load it.
        if self.existsDB():
            if not self.setMeal():
                print(f"Meal: Meal Id <{self.getMealId()}> is invalid ")
        else:
            self.save()

    def setMeal(self, mealId=None):
        '''Set the meal attributes with values from database for a mealid'''
        retcode=False
        if mealId:
            self.getMealId(mealId)

        if self.getMealId():
            sql = f"SELECT mealId, mealName, mealPrice, courseId FROM meals WHERE mealId = {self.getMealId()}"

            mealData = self.dbGetData(sql)
            for meal in mealData:
                self.setMealId(meal['mealId'])
                self.setMealName(meal['mealName'])
                self.setMealPrice(meal['mealPrice'])
                self.setCourseId(meal['courseId'])
                self.setCourse()
                #self.setCourse(Course.Course(courseId=self.getCourseId()))

            retcode =True
        return retcode
    
    #getters/setters of attributes
    def setMealId(self,mealId=None):
        self.__mealId = mealId

    def setMealName(self, mealName= None):
        self.__mealName = mealName

    def setMealPrice(self, mealPrice=None):
        self.__mealPrice = mealPrice
    
    def setCourseId(self, courseId= None):
        self.__courseId = courseId
    def setCourse(self, course=None):
        '''Save the owning Course for this meal = hi directional association'''
        if course:
            self.__course = course
            self.setCourseId(self.__course.getCourseId())
        else:
            if self.getCourseId():
                course =  Course.Course(courseId=self.getCourseId())
                self.setCourse(course)
            else:
                self.__course = None 
       
    def getMealId(self):
        return self.__mealId
    def getMealName(self):
        return self.__mealName
    def getMealPrice(self):
        return self.__mealPrice
    def getCourseId(self):
        return self.__courseId
    def getCourse(self):
        return self.__course
    
    def __str__(self):
        '''Return a stringfield version of object for print functions
            - mauy be same or different from display() method'''
        return f"Meal: <{self.getCourseId():2d}-{self.getMealId():2d}> {self.getMealName().title():20s} ${self.getMealPrice():5.2f}"
    def display(self):
        '''Format display Meal'''
        print(f"Meal: <Course{self.getCourseId():2d} {self.getCourse().getCourseName().title()}, Meal:{self.getMealId():2d}> {self.getMealName().title():20s} ${self.getMealPrice():5.2f}")

    def existsDB(self):
        '''Check if object already exists in datbase'''
        retcode=False
        # Ise Primary Key to check if the meal exists inDB
        if self.getMealId():
            sql = f"SELECT count(*) AS count FROM meals WHERE mealId={self.getMealId()}"
            # print(sql)
            countData = self.dbGetData(sql)
            if countData:
                for countRec in countData:
                    count = int(countRec['count'])
                if count > 0:
                    retcode = True
        return retcode
    
    def save(self):
        '''Save meal data back to the database'''

        if self.getCourse():
            self.setCourseId(self.getCourse().getCourseId())
        if self.existsDB():
            sql = f'''UPDATE meals SET
                mealId={self.getMealId()},
                mealName={self.getMealName()}, 
                mealPrice={self.getMealPrice()},
                courseId={self.getCourseId()},
                WHERE mealId={self.getMealId()}
            '''
            self.dbChangeData(sql)

        else:
            sql = f'''
                INSERT INTO meals
                (mealName, mealPrice, courseId)
                VALUES
                ('{self.getMealName()}', {self.getMealPrice()}, {self.getCourseId()})
                '''
                #SAVE NEW PRIMARY KEY

            self.setMealId(self.dbPutData(sql))

    def delete(self):
        '''delete meal from database'''
        pass    

    @classmethod
    def getMeals(cls, course):
        ''''Get Meals for a course object or instance - example of aggregation'''
        meals = []
        if course:
            sql = f"SELECT mealId, mealName, mealPrice, courseId FROM meals WHERE courseId = {course.getCourseId()}"
            # print(f"test all meals: {sql}")

            mealsData = SPXCafe().dbGetData(sql)

            for mealData in mealsData:
                # create a new instance
                meal = cls.__new__(cls)
                meal.setMealId(mealData['mealId'])
                meal.setMealName(mealData['mealName'])
                meal.setMealPrice(mealData['mealPrice'])
                meal.setCourseId(mealData['courseId'])
                meal.setCourse(course)
                meals.append(meal)
        return meals
    
    def findMeal(self, searchMeal=None):
        if searchMeal:
            if self.isMatch(searchMeal):
                return self
        return None
    
    def isMatch(self, mealName= None):
        confidence = partial_ratio(mealName, self.getMealName())
        # print(confidence, self.getMealName())
        if confidence >80:
            return True
        else:
            return False

    # def findMealByName(self, mealName=None):
    #     '''find Meals using there Names'''
    #     mealList = []
    #     sql = None
    #     if mealName:
    #         sql = f"SELECT mealId, mealName, mealPrice, courseId FROM meals WHERE mealName = '{mealName}'"
    #         mealData = self.dbGetData(sql)
    #         for meals in mealData:
    #             self.setMealId(meals['mealId'])
    #             self.setMealPrice(meals['mealPrice'])
    #             mealList.append(self.getMealId())
    #             mealList.append(self.getMealPrice())
    #         return mealList
    # def findMealName(self, mealId = None):
    #     '''gets the mealName form mealId'''
    #     sql = None
    #     sql = f'''SELECT mealId, mealName, mealPrice, courseId 
    #         FROM meals 
    #         WHERE mealId = '{mealId}'
    #         ORDER BY mealId
    #         '''
    #     mealData = self.dbGetData(sql)
    #     for meals in mealData:
    #         self.setMealName(meals['mealName'])
    #     return self.getMealName()
def main():
    meal = Meal(1)       # retrieve existiing meal
    meal.display()
    # meal.display()              #show existing values
    # meal.setMealPrice(meal.getMealPrice()+1) #update meal data demo
    # meal.save()                 #save meal again from Db
    # meal.Meal(mealId=1)            #show ammend meal
    # meal.display()

    
    # print("Creating New meal not in database.....")
    # #create a new meal completely 
    # meal = meal(mealName="Salata2", mealPrice=3.45, courseId=1)
    # meal.display()
    searchMeal = input("streak")
    if meal.isMatch(searchMeal):
        print('match')
    else:
        print("not matched")
    foundMeal = meal.findMeal(searchMeal)
    if foundMeal:
        foundMeal.display()
if __name__ == "__main__":
    main()

