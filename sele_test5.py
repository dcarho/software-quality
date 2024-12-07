from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://resultadodelaloteria.com/colombia/loteria-del-meta")
numberList = browser.find_elements(By.CLASS_NAME, 'ball')
numberListSm = browser.find_elements(By.CLASS_NAME, 'ballSm')

for number in numberList:
  print(number.text)

for number in numberListSm:
  print(number.text)

browser.quit()