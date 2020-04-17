#-*- coding:utf-8 -*-

from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests
import json
#pip install flask_cors
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/crawling', methods=['post'])
def crawling():
    #naver movie list를 crawling해오자
    
    resp = requests.get('https://movie.naver.com/movie/running/current.nhn')
    soup = BeautifulSoup(resp.text, 'html.parser')  #html.parser를 붙이는 이유 : 
    
    

    movies = soup.find_all('dl', class_='lst_dsc')
    
    #crawling 된 데이터를
    #{movie:[{title:제목, star:별점}....]}로 저장하자
    


    lst = list()

    for movie in movies:
        title = movie.find('a').text
        star = movie.find('span',class_='num').text
    
        tmp = {}
        tmp['title'] = title
        tmp['star'] = star
    
        lst.append(tmp)
    
    
    res = {}
    res['movies'] = lst
    res_json = json.dumps(res, ensure_ascii=False)

    #print(res_json)

    return res_json
    
   
    #json으로 변환하여 리턴하자
 



if __name__ == '__main__':
    app.run('localhost', port='8585')