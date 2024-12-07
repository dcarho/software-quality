from selenium import webdriver
from warnings import filterwarnings
filterwarnings("ignore")

browser = webdriver.Chrome(executable_path="./drivers/chromedriver")
browser.get('https://resultadodelaloteria.com/')
resultList = browser.find_element_by_id('ctl00_ulColombia')
linkList = resultList.find_elements_by_tag_name('a')
for link in linkList:
	print("Nombre: %s / Link: %s" % (link.text, link.get_attribute('href')))
browser.quit()