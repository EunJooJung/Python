#-*- coding:utf-8 -*-

import pickle

score = {'name':'kh', 'kor':100, 'eng':40, 'math':60}  #dic 타입

with open('test02.txt','wb') as file:   #바이너리타입으로 읽어준 것 
    pickle.dump(score, file)
    
'''
pickling : 객체 -> 파일
unpickling : 파일 -> 객체

'''
