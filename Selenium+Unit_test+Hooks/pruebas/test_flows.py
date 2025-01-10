from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import unittest
from ..flows import sele_flows as flows

from time import sleep

class flows_test(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.sauceListUsers = ["standard_user","locked_out_user","problem_user","performance_glitch_user","error_user","visual_user"]
        self.sauceListPrices =["$29.99", "$9.99", "$15.99", "$49.99", "$7.99", "$15.99"]
        self.sauceSecret = "secret_sauce"
        self.sauceUser = "standard_user"       

    
    def tearDown(self):
        
        sleep(10)
        try:
            self.browser.quit()
        except:
            return
    
    def test_getSauseDemoUsers(self):
        
        browser = self.browser
        browser.get("https://www.saucedemo.com/")
        
        div = browser.find_element(By.ID, 'login_credentials')
        resul = div.text
        
        users = resul.split("\n")
        users.pop(0)

        self.assertListEqual(self.sauceListUsers, users,"Falló: La lista de usuarios no coincide.")

    
    def test_getSausePassword(self):

        browser = self.browser
        browser.get("https://www.saucedemo.com/")
        
        div = browser.find_element(By.CLASS_NAME, 'login_password')
        password = div.text.split("\n")[1]
        
        self.assertEqual(password, self.sauceSecret, "Falló: La clave no coincide.")
    
    
    def test_doLoginSause(self):

        browser = self.browser
        browser.get("https://www.saucedemo.com/")

        fname = browser.find_element(By.NAME, "user-name")
        fname.clear()
        fname.send_keys(self.sauceUser)

        passwd = browser.find_element(By.ID, "password")
        passwd.clear()
        passwd.send_keys(self.sauceSecret)

        submitButton = browser.find_element(By.NAME, 'login-button')
        submitButton.send_keys(Keys.ENTER)

        sleep(1)
        
        div_header = browser.find_element(By.CLASS_NAME, 'title')
        text = div_header.text
        
        self.assertEqual(text, "Products", "Falló: El titulo secundario no es \"Products\".")

    def test_goCart(self):
        
        result = flows.goCart()
        self.assertEqual(result, "Your Cart", "Falló: El titulo secundario no es \"Your Cart\"." )


    def test_getSauseListPrices(self):
        
        result = flows.getSauseListPrices()
        self.assertListEqual(result,self.sauceListPrices,"Falló: La lista de precios no coincide.")

if __name__ == '__main__':
    unittest.main()