from selenium import webdriver
import time

from warnings import filterwarnings
filterwarnings("ignore")

browser = webdriver.Chrome()
browser.get("http://google.com.co")
browser.get_screenshot_as_file("test.png")
#browser.quit()

