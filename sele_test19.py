from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

from warnings import filterwarnings
filterwarnings("ignore")

browser = webdriver.Chrome()
browser.get("http://the-internet.herokuapp.com/dropdown")
dropdown = browser.find_element(By.ID, "dropdown")
optionList = dropdown.find_elements(By.TAG_NAME, "option")

for option in optionList:
	print(option.get_attribute("value"))

dropdownAction = Select(browser.find_element(By.ID, "dropdown"))
dropdownAction.select_by_value("2")
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
