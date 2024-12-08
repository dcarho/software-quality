from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from warnings import filterwarnings
filterwarnings("ignore")

browser = webdriver.Chrome()

browser.get("https://demo.guru99.com/test/login.html")
fname = browser.find_element(By.ID, "email")
fname.clear()
fname.send_keys('Daniel')
lname = browser.find_element(By.ID, "passwd")
lname.clear()
lname.send_keys('Fernando')
submitButton = browser.find_element(By.ID, 'SubmitLogin')
submitButton.send_keys(Keys.ENTER)



try:
    print("Navegador abierto. Presiona Ctrl+C para salir.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nCerrando navegador...")
    browser.quit()

