from selenium import webdriver

browser = webdriver.Chrome()

urls = ['https://www.duckduckgo.com', 'https://google.com', 'https://es.wikipedia.org/wiki/Wikipedia:Portada']
for url in urls:
  browser.get(url)
  print("Titulo: %s" % browser.title)

browser.quit()