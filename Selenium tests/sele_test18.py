from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from warnings import filterwarnings
filterwarnings("ignore")

browser = webdriver.Chrome()
browser.get("https://www.w3schools.com/howto/howto_css_switch.asp")
switch = browser.find_element(By.XPATH, "//*[@id='main']/label[3]/div")
switch.click()
time.sleep(3)
switch.click()
time.sleep(3)

#browser.quit()

