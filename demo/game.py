

import random
import time

lis=['paper','stone','scissors']
pc=0
user=0
tie=0

i=1
while i<=10:

    print('')
    print(f'............Round{i}..............\n')

    inp=input('Enter Your Action :- ').lower()
    lis1=random.choice(lis)

    print('')
    print(""".........Now Wait 
      for PC action.........\n""")

    time.sleep(2)
    print("PC's action : ",lis1,)

    if inp==lis1:
        tie+=1
    elif (inp=='paper' and lis1=='scissors') or(inp=='stone' and lis1=='paper') or(inp=='scissors' and lis1=='stone'):
        pc+=1
    else:
        user+=1

    i+=1

print('PC Score :',pc)
print('Your Score :',user)
print('Tie Score :',tie)

if pc>user:
    print('You are Loss ')
elif user>pc:
    print('Congratulations !!! Tou Win the game....')
else:
    print('Tie')        

