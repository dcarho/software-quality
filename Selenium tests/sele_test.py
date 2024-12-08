from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://www.google.com.co")
#browser.implicitly_wait(0.5)
print("Titulo: %s" % browser.title)

browser.quit()