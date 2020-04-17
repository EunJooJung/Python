#-*- coding:utf-8 -*-

# pip install selenium
from selenium import webdriver
from bs4 import BeautifulSoup

tag = input('search tag : ')
url = 'https://www.instagram.com/explore/tags/'+tag

#chrome version에 맞는 web driver 필요!
driver = webdriver.Chrome('C:/test/chromedriver.exe')


driver.implicitly_wait(3) #조금 기다렸다가 화면이 만들어지면 가져와 주세요
driver.get(url)

soup = BeautifulSoup(driver.page_source,'html.parser')
div = soup.find_all('div',class_='KL4Bh')
print(div)