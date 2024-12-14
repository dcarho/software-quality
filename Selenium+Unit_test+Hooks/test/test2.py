# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from time import sleep
from selenium.webdriver.common.by import By

class eis_test(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def test_load(self):
		browser = self.browser
		browser.get("http://demo.guru99.com/test/login.html")
		fname = browser.find_element(By.ID, 'email')
		fname.clear()
		fname.send_keys('Daniel')
		lname = browser.find_element(By.ID, 'passwd')
		lname.clear()
		lname.send_keys('Fernando')
		submitButton = browser.find_element(By.ID, 'SubmitLogin')
		submitButton.send_keys(Keys.ENTER)
		sleep(2)
		res = browser.find_element(By.XPATH, '//html/body/div[2]/div/div/h3')
		self.assertEqual('Successfully Logged in...', res.text)

	def tearDown(self):
		print()
		#self.browser.quit()

if __name__ == '__main__':
	unittest.main()