from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from warnings import filterwarnings
filterwarnings("ignore")

browser = webdriver.Chrome()

browser.get("http://the-internet.herokuapp.com/checkboxes")
time.sleep(3)
checkboxOne = browser.find_element(By.XPATH, "//*[@id='checkboxes']/input[1]")
checkboxOne.click()
time.sleep(3)
checkboxTwo = browser.find_element(By.XPATH, "//*[@id='checkboxes']/input[2]")
checkboxTwo.click()
#browser.quit()


'''
try:
    print("Navegador abierto. Presiona Ctrl+C para salir.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nCerrando navegador...")
    browser.quit()
'''

