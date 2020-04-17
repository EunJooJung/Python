#-*- coding:utf-8 -*-

# x와 y를 입력하면 2 * x + y 값을 리턴하는 mysum() 함수를 만들자.

# main에서 호출

def mysum(x, y):
    return 2 * x + y

if __name__ == '__main__':
    print(mysum(2, 3))

    b = lambda x,y : 2 * x + y
    print(b(2,3))

