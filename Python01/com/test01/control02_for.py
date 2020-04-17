#-*- coding:utf-8 -*-

subject = ['java', 'javascript', 'python']
for i in subject:
    print(i)

#반복문 수행이 끝난 후 else를 실행함, end 붙여주면 반복마다 끝에 붙음
for i in subject:
    print(i, end=' ')
else:
    print('\n재밌다.')

for i in range(1, 100):
    print(i, end=',')
else:
    print(100)

print('----------')
print('<<구구단>>')


for i in range(2,10):
    print('<'+str(i)+'단>')
    for j in range(1,10):
        print(i,'*',j,'=',(i*j), sep=' ')
    print()
        
        
for i in range(10,0,-1):
    print(i)
        