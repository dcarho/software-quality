from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()

browser.get("https://www.random.org/strings/?num=1&len=20&digits=on&upperalpha=on&loweralpha=on&unique=on&format=html&rnd=new")
dataElement = browser.find_element(By.CSS_SELECTOR, 'pre.data')
print("String generado: %s" % dataElement.text)
browser.quit()
