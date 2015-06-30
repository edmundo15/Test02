'''
Created on Jun 25, 2015

@author: Edmundo Cossio
'''
from selenium.webdriver.support import expected_conditions as EC
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By

from Singleton.DriverManager import DriverManager
from Singleton.GlobalVar import HomePageURL


class CreateAccount:
    __driver = None
    __wait = None        
    __register_button = (By.CSS_SELECTOR, "div.buttons-set > button.button")
    __create_account_form = (By.ID, "form-validate")
    __validate_hello = (By.CSS_SELECTOR, "p.hello > strong")
    __firstname_text = (By.ID, "firstname")
    __lastname_text = (By.ID, "lastname")
    __email_address_text = (By.ID, "email_address")
    __password_text = (By.ID, "password")
    __confirmation_text = (By.ID, "confirmation")
    
    
    def __init__(self):                        
        self.__driver = DriverManager().get_instance().get_driver()
        #self.open_browser(HomePageURL)
        self.__wait = DriverManager().get_instance().get_wait()
        
    def create_new_account(self, firstName, lastName, emailAddress, passw, confirmPassw):                
        self.__wait.until(EC.visibility_of_element_located(self.__create_account_form), "Error,")
        #self.__wait.until(EC.presence_of_all_elements_located(self.__create_account_form), "Error,")        
        self.__driver.find_element(*self.__firstname_text).send_keys(firstName)
        self.__driver.find_element(*self.__lastname_text).send_keys(lastName)
        self.__driver.find_element(*self.__email_address_text).send_keys(emailAddress)
        self.__driver.find_element(*self.__password_text).send_keys(passw)
        self.__driver.find_element(*self.__confirmation_text).send_keys(confirmPassw)
        
    def click_register(self):
        self.__driver.find_element(*self.__register_button).click()
        
    def validate_if_the_My_Dashboard_page_is_displayed(self, firstname, lastname):
        self.__wait.until(EC.visibility_of_element_located(self.__validate_hello), "Error,")
        actual_result = self.__driver.find_element(*self.__validate_hello).text
        expected_result =  "Hello, "+firstname+" "+lastname+"!"
        BuiltIn().should_be_equal(actual_result, expected_result, 'Error, the message is not displayed: ' + "Invalid login or password.")