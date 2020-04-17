#-*- coding:utf-8 -*-

# 함수 작성 -> def 함수명(파람):

def func01():
    pass
#함수 안에 아무것도 없다


def func02():
    print('함수 02 입니다.')
    

def func03():
    return '함수 03 입니다.'


def func04():
    return {1:'a',2:200}


if __name__=='__main__':
    # main: 프로그램의 주 진입점 (__언더바가 붙어 있으면 해당 클래스 안에서만 사용했으면 좋겠다.)
    print(func02()) #python에서 none이란 아무것도 없다 ex>null
    str01 = func03()
    print(str01)
    print(func04()[1]) #키가 1인 애를 가지고 와라는 의미 dictionary
    
    
