#-*- coding:utf-8 -*-

hap01 = lambda a,b: a + b
print(hap01)
print(hap01(10,20))



gob = lambda a, b: a*b
print(gob(10,20))


hap02 = lambda a,b,c: a+b+c
print(hap02(1,2,3))


a = [(1, 'one', 9),(2, 'two',  8), (3, 'three', 7),(4, 'four', 6)]
a.sort(key=lambda a:a[1])
print(a)

min01 = (lambda x,y : x if x < y else y)(11,22)
print(min01)

max01 = (lambda x,y : x if x > y else y)
print(max01(33,44))


b = lambda x : (lambda newx : x + newx)
c = b(100)
d = c(90)
print(d)
print(b(100)(90))


# 1 ~ 100 사이의 숫자 중, 5의 배수만 출력하자.
e = lambda x : bool(x % 5)
five =[i for i in range(1,101) if not e(i)]
print(five)


f = lambda x: x if (x%5 !=0) else None
res = [i for i in range(1,101) if not f(i)]

result = [i for i in range(1, 101) if not (lambda x : x if(x % 5 != 0) else None)(i)]
print(result)


