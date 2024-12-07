from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from warnings import filterwarnings
filterwarnings("ignore")


browser = webdriver.Chrome(executable_path="./drivers/chromedriver")
browser.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")
divResults = browser.find_element_by_id("main-tfa")
title = divResults.find_element_by_css_selector("h2.main-box-header a")
image = divResults.find_element_by_css_selector("div.floatright img")
textList = divResults.find_elements_by_tag_name("p")
print("Title -> %s" % title.text)
print("Url -> %s" % title.get_attribute('href'))
print("Imagen -> %s" % image.get_attribute('src'))
for text in textList:
	print(text.text)
browser.quit()

