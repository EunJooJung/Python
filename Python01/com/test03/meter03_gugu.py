#-*- coding:utf-8 -*-


# 1. for문을 사용하여 구구단 전체를 출력하는 gugu()함수를 만들자.
# 2. while문을 사용하여 입력된 숫자의 단만을 출력하는  gugudan(x)를 만들자.
# 3. main 만들어서 위의 두 함수를 호출하자.


def gugu():
    for i in range(2,10):
        for j in range(2,10):
            print('%d * %d =' %(i, j) ,i*j)




def gugudan():
    x = input('x 입력 :')
    
    for i in range(2,10):
        print('%d * %d =' %(int(x),i), int(x)*i)



def guguwile(x):
    print(str(x)+'단')
    i=1
    while i<10:
        print('{} * {} = {}'.format(x, i, x*i))
        i+=1
        
        

if __name__ == '__main__':
    gugu()
    #gugudan()
    guguwile(3)
                            