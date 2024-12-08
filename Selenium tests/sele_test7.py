from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from warnings import filterwarnings
filterwarnings("ignore")


def semestre(level, label):
	divResults = browser.find_element_by_id(label)
	tbody = divResults.find_element_by_tag_name('tbody')
	linkList = tbody.find_elements_by_tag_name('tr')
	print("%s\n" % level)
	for link in linkList:
		course = link.find_elements_by_tag_name('td')[1].text
		print(course)
	print("----------------")

browser = webdriver.Chrome(executable_path="./drivers/chromedriver")
browser.get("http://fcbi.unillanos.edu.co/fcbi/eis/")
semestre("Semestre 1", 'href1')
#semestre("Semestre 2", 'href2')
browser.quit()

