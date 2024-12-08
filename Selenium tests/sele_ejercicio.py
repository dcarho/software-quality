from selenium import webdriver
from selenium.webdriver.common.by import By

#browser = webdriver.Chrome()
browser = webdriver.Firefox()

browser.get("https://campusvirtualunillanos.co/")

clases = browser.find_elements(By.CLASS_NAME, 'h-100')

for clase in clases:
    
    p = clase.find_element(By.TAG_NAME,'h3')  
    print(p.text)
    print('-----------------')

browser.quit()
