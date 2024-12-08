from selenium import webdriver
import time

from warnings import filterwarnings
filterwarnings("ignore")

browser = webdriver.Chrome()
browser.get("https://google.com/")
time.sleep(2)
browser.get("https://facebook.com/")
time.sleep(2)
browser.get("https://x.com/")
time.sleep(2)
browser.back()
time.sleep(2)
browser.back()
time.sleep(2)
browser.forward()
#browser.quit()

try:
    print("Navegador abierto. Presiona Ctrl+C para salir.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nCerrando navegador...")
    browser.quit()
