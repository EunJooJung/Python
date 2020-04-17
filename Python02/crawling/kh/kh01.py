#-*- coding:utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://iei.or.kr/intro/teacher.kh'

driver = webdriver.Chrome('C:/test/chromedriver.exe')

driver.implicitly_wait(3)
driver.get(url)

soup = BeautifulSoup(driver.page_source,'html.parser')
div = soup.find_all('div', class_='intro_thum')

donghun = div.select('img')[8].text

print(donghun)

