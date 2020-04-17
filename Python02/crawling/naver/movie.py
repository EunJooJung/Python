#-*- coding:utf-8 -*-

# pip install beautifulsoup4  요청해서 응답하는 건 얘가 하는 게 아니다.
from bs4 import BeautifulSoup
import urllib.request

resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn#')
soup = BeautifulSoup(resp, 'html.parser')

#print(soup)
#print(soup.find('dl'))

movies = soup.find_all('dl',class_='lst_dsc')
#print(movies[0])

for movie in movies:
    title = movie.find('a').text
    star = movie.find('span',class_='num').text
    print('{} [{}]'.format(title,star))
    
for movie in movies:
    star = movie.find('span',class_='num').text
    #print(star)