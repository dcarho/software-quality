from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

urlGeneral = 'https://resultadodelaloteria.com/colombia/'
urls = ['loteria-del-huila', 'loteria-del-meta', 'loteria-de-medellin']

for url in urls:
	print("Resultado -> %s" % url)
	print("%s%s" % (urlGeneral, url))

	browser.get("%s%s" % (urlGeneral, url))
	numberList = browser.find_elements(By.CLASS_NAME, 'ball')
	numberListSm = browser.find_elements(By.CLASS_NAME, 'ballSm')

	for number in numberList:
	  print(number.text)

	for number in numberListSm:
	  print(number.text)

	print("---------------")

browser.quit()