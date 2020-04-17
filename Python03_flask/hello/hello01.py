#-*- coding:utf-8 -*-

# pip install flask

from flask import Flask
app = Flask(__name__)


@app.route('/') #@app.route로 url mapping한다 루트로 요청이 들어오면 return된다.
def hello():
    return "hello, Flask!"



if __name__ == '__main__':
    app.run()

# 콘솔창에 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) 이게 뜨고
# http://127.0.0.1:5000/로 접속하면 hello, Flask! 가 뜬다.

