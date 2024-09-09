#Rendom number

import random

Rnum = random.randint(1, 100)

while True:
    usernum = (input('Gess the number :or Quit(q) '))
    if(usernum == 'q'):
        break
    usernum = int(usernum)
    if(usernum == Rnum):
        print('You completed the game')
        break
    elif (usernum < Rnum):
        print('your number was Small')
    else:
        print('your number was Big')
        
print('----GAME OVER---')