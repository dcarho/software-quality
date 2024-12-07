from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

from warnings import filterwarnings
filterwarnings("ignore")

browser = webdriver.Chrome()

browser.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(1)
#browser.quit()

try:
    print("Navegador abierto. Presiona Ctrl+C para salir.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nCerrando navegador...")
    browser.quit()

