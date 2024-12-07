from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from warnings import filterwarnings
filterwarnings("ignore")

browser = webdriver.Chrome()

browser.get("https://google.com/")
element = WebDriverWait(browser, 10).until(
	EC.presence_of_element_located((By.NAME, "q"))
	)
#browser.quit()


'''
try:
    print("Navegador abierto. Presiona Ctrl+C para salir.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nCerrando navegador...")
    browser.quit()
'''


