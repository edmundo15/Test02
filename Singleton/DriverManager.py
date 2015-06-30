'''
Created on Jun 23, 2015

@author: Edmundo Cossio
'''
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class Singleton:
    def __init__(self, klass):
        self.klass = klass
        self._instance = None

    def __call__(self, *args, **kwds):
        if self._instance is None:
            self._instance = self.klass(*args, **kwds)
        return self._instance

@Singleton
class DriverManager():
    _driver = None
    _wait = None
    _instance = None    

    def __init__(self):        
        self.initialize_webdriver()    
            
    def createNewIEsession(self):                
        dir = os.path.dirname(__file__)
        ie_driver_path = dir + "\IEDriverServer.exe"        
        self._driver = webdriver.Ie(ie_driver_path)

    def initialize_webdriver(self):
        try:         
            if self._driver is None:                        
                self._driver = webdriver.Firefox()    
                #self.createNewIEsession()                                        
                self._driver.implicitly_wait(float(30))
                self._driver.maximize_window()
                self._wait = WebDriverWait(self._driver, float(30))                
        except TypeError as e:
            print e.message

    def get_instance(self):
        if self._instance is None or self._driver is None:
            self._instance = DriverManager()
        return self._instance

    def get_driver(self):
        return self._driver

    def get_wait(self):
        return self._wait