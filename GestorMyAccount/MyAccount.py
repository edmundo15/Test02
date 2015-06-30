'''
Created on Jun 23, 2015

@author: Edmundo Cossio
'''
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Singleton.DriverManager import DriverManager
from Singleton.GlobalVar import HomePageURL


class MyAccount:
    __driver = None
    __wait = None    
    __account_link = (By.LINK_TEXT, "ACCOUNT")
    __loggin_button = (By.NAME, "send")
    __pass_textbox = (By.ID, "pass")
    __email_textbox = (By.ID, "email")
    __invalid_pass_label = (By.CSS_SELECTOR ,"li > span")
    __create_account_link = (By.LINK_TEXT, "Create an Account")
    
    def __init__(self):                        
        self.__driver = DriverManager().get_instance().get_driver()
        #self.open_browser(HomePageURL)
        self.__wait = DriverManager().get_instance().get_wait()
        
    def select_a_link_of_my_account_menu(self,valor):
        self.__wait.until(EC.visibility_of_element_located(self.__account_link), "Error,")                              
        #self.__driver.find_element(self._account_link).click()
        self.__driver.find_element(By.LINK_TEXT, "ACCOUNT").click()         
        self.__driver.find_element(By.LINK_TEXT, valor).click()        
    
    def set_account_crendetials(self, email, password):
        self.__set_email_address(email)
        self.__set_password(password)
    
    def __set_email_address(self, email):          
        self.__driver.find_element(*self.__email_textbox).send_keys(email)        

    def __set_password(self, password):          
        self.__driver.find_element(*self.__pass_textbox).send_keys(password)        
    
    def click_login(self):                  
        self.__driver.find_element(*self.__loggin_button).click()        
    
    def click_create_account(self):                  
        self.__driver.find_element(*self.__create_account_link).click()                       
                
    def validate_if_the_invalid_credentialsMSG_is_displayed(self):
        self.__wait.until(EC.visibility_of_element_located(self.__account_link), "Error,")     
        actual_result = self.__driver.find_element(*self.__invalid_pass_label).text
        expected_result =  "Invalid login or password."
        BuiltIn().should_be_equal(actual_result, expected_result, 'Error, the message is not displayed: ' + "Invalid login or password.")
     
          