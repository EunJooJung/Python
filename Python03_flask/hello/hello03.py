#-*- coding:utf-8 -*-

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_root():
    return'<a href="/test/admin">id</a>'

@app.route('/test/<id>') #<>안에 있는 것을 파라미터로 전달
def hello_id(id):
    return '<h1>hello,'+id+'</h1>'


if __name__ == '__main__':
    app.run()
    
