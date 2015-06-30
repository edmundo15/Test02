'''
Created on Jun 25, 2015

@author: Edmundo Cossio
'''
from Singleton.DriverManager import DriverManager
from Singleton.GlobalVar import HomePageURL


#===============================================================================
# global driver
# global wait
# 
# def open_browser1():
#     driver = DriverManager().get_instance().get_driver()
#     open_browser(HomePageURL)
#     wait = DriverManager().get_instance().get_wait()
#     
# def close_browser1():
#     driver.close()
#===============================================================================
    
class SetUp():  
    __driver = None
    __wait = None    
    
    def __init__(self):                        
        self.__driver = DriverManager().get_instance().get_driver()        
        self.__wait = DriverManager().get_instance().get_wait()
              
    def open_browser(self):        
        self.__driver.get(HomePageURL)    
    
    def close_browser(self):        
        self.__driver.close()
