#-*- coding:utf-8 -*-


def coffee(m, c):
    # 잔돈 계산 / 넣은 돈 - 잔수 * 커피가격
    # prn 호출(커피 잔 수, 잔돈)
    
    jandone = m - c * 300
        
    prn(c,jandone)
    
    
    

def prn(c=0, jandone=0):
    # 출력
    # 커피 x 잔이 나왔습니다. 잔돈은 x원 입니다. 
    # 돈이 부족합니다. 
    if jandone < 0 :
        print('금액이 부족합니다.')

    else : 
        print('커피  %d잔이 나왔습니다. 잔돈은 %d원 입니다.' %(c, jandone))
        



           
def start():
    # 커피 잔 수 입력  q= int(input('커피 몇 전이 필요하신가요 : '))
    # 돈 입력 p = int(input('=돈을 넣어주세요 (300) : '))
    # coffee 함수에 잔수와 돈 전달하면서 호출
    
    m = input('돈을 넣어주세요 : ') 
    c = input('커피를 몇잔 주문하시겠습니까? (300) : ')
    
    coffee(int(m),int(c))


if __name__ == '__main__':
    
    start()