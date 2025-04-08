import random
randnum = random.randint(1,5)
 
while True :
    asknum =  int(input('give a number:  '))
   
    if(asknum > 5):
        print('your number is too high ')
        print('try again')
 
    elif(asknum < 1 ):
        print('your number is too low')
        print('try again')


    elif asknum == randnum :
        print('congrates !!!!!!')
        break