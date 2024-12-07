from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from warnings import filterwarnings
filterwarnings("ignore")

browser = webdriver.Chrome()
browser.get("http://www.google.com")

all_cookies=browser.get_cookies();
cookies_dict = {}
for cookie in all_cookies:
	cookies_dict[cookie['name']] = cookie['expiry']
print(cookies_dict)
browser.quit()