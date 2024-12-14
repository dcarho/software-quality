from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from warnings import filterwarnings
filterwarnings("ignore")
import unittest

class eis_test(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def test_load(self):
		urlGeneral = 'https://resultadodelaloteria.com/colombia/'
		urls = ['loteria-del-huila', 'loteria-del-meta', 'loteria-de-medellin']

		for url in urls:
			print("Resultado -> %s" % url)
			print("%s%s" % (urlGeneral, url))
			self.browser.get("%s%s" % (urlGeneral, url))
			numberList = self.browser.find_elements(By.CLASS_NAME, 'ball')
			res = []
			for number in numberList:
				res.append(number.text)
			self.assertEqual(len(res), 3, msg='Fallo en el resultado de -> %s' % (url))

	def tearDown(self):
		self.browser.quit()

if __name__ == '__main__':
	unittest.main()