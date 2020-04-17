#-*- coding:utf-8 -*-

#lotto

import random

def lotto():
    lotto = set()
    
    while len(lotto) <= 5:
        ran = random.randint(1,45)
        lotto.add(ran)
    #print(list(lotto)) list로 변환하면 순서 정렬
    lst = sorted(lotto) #sorted 함수 안에 넣으면 자동으로 정렬 됨
    print(lst)

if __name__ == '__main__':
    lotto()
