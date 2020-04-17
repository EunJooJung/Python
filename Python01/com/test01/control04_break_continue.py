#-*- coding:utf-8 -*-

i=1
while i<=10:
    if i>5:
        break
    print(i)
    i+=1
else:
    print('i:'+str(i))
#break로 인해 while문이 정상적으로 종료되지 않았기에 else 작동x

for i in range(1,10):
    if i%2==0:
        continue
    print(i)
else:
    print('i',i,sep=':')

    