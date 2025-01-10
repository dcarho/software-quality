from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep

browser = None

def getSauseDemoUsers():
    
    browser = webdriver.Chrome()
    browser.get("https://www.saucedemo.com/")

    div = browser.find_element(By.ID, 'login_credentials')
    resul = div.text
    users = resul.split("\n")
    users.pop(0)
    #standard_user
    #locked_out_user
    #problem_user
    #performance_glitch_user
    #error_user
    #visual_user    

    browser.quit()
    return users

def getSausePassword():

    browser = webdriver.Chrome()
    browser.get("https://www.saucedemo.com/")
    
    div = browser.find_element(By.CLASS_NAME, 'login_password')
    password = div.text.split("\n")[1] #secret_sauce
    
    browser.quit()

    return password

def doLoginSause(user, password, quiteBrowser=True):

    global browser
    browser = webdriver.Chrome()
    browser.get("https://www.saucedemo.com/")

    fname = browser.find_element(By.NAME, "user-name")
    fname.clear()
    fname.send_keys(user)

    passwd = browser.find_element(By.ID, "password")
    passwd.clear()
    passwd.send_keys(password)

    submitButton = browser.find_element(By.NAME, 'login-button')
    submitButton.send_keys(Keys.ENTER)

    sleep(2)
    
    title = browser.find_element(By.CLASS_NAME, 'title')
    text = title.text

    if(quiteBrowser):
        browser.quit()        

    return text == "Products"
    


def getSauseListPrices():

    prices = []
    
    doLoginSause("standard_user", "secret_sauce", False) 
    
    if browser is not None:
        div_prices = browser.find_elements(By.CLASS_NAME, 'inventory_item_price')
        for div in div_prices:
            prices.append(div.text)
        browser.quit()

    return prices


def goCart():

    doLoginSause("standard_user", "secret_sauce", False)    
    
    cart_link = browser.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_link.click()
    sleep(1)
    
    text = ""
    
    if browser is not None:
        div_header = browser.find_element(By.CLASS_NAME, 'header_secondary_container')
        text = div_header.text
        browser.quit()

    return text #Your Cart

#getSauseListPrices()
#getSausePassword()
goCart()