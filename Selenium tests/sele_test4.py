from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://www.dannybrien.com/random/")

table = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/table')

rows = table.find_elements(By.TAG_NAME, 'tr')

for row in rows:
    cells = row.find_elements(By.TAG_NAME, 'td')
    for cell in cells:
        print(cell.text)
    print('-----------------')

browser.quit()
