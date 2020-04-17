# -*- coding:utf-8 -*- 
#5! = 5*4*3*2*1


def factorial(n):
    res = 1
    for i in range(i, n+1):
        res *= i
    return res
        
    
    
   

def factorialRecursion(n):

    pass



if __name__ == '__main__':
    n = int(input('n:'))
    res = factorialRecursion(n)
    print('{} factorial = {}'.format(n, res))
    print('{} factorial = {}'.format(n, factorial(n)))