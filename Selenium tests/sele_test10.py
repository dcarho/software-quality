from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from warnings import filterwarnings
from time import sleep
filterwarnings("ignore")

browser = webdriver.Chrome(executable_path="./drivers/chromedriver")
browser.get('https://www.google.com')
searchInput = browser.find_element_by_class_name('gLFyf')
searchInput.send_keys("Unillanos" + Keys.ENTER)
sleep(7)
browser.quit()
