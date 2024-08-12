from database import Database
from datetime import datetime

class SPXCafe(Database):
    '''# Wrapper Class around Database specific for SPXCAfe Database'''
    def __init__(self):
        '''COnstructor method - defaults spxcafe datbase'''

        self.__dbname = "SPXcafe2.db"
        super().__init__(self.__dbname)

    def getToday(self):
        return datetime.today().date().strftime('%Y-%m-%d') 
    #ISO format for dates -  how splits as well mysql stores data