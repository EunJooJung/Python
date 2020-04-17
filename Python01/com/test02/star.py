#-*- coding:utf-8 -*-





'''
     *
     **
     ***
     ****
     *****
'''

for i in range(5):
    print('*'*(i+1))
    
print('------')

print('\n'.join([''.join(['*'for i in range(i+1)])for i in range(5)]))

print('------')


'''
     *****
     ****
     ***
     **
     *
'''


for i in range(5):
    print('*'*(5-i))
    
print('------')    
    
print('\n'.join([''.join(['*'for i in range(5-i)])for i in range(5)]))

print('------')  

'''
          *
         ***
        *****
       *******
      *********
'''
    