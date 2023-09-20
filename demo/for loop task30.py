
from datetime import datetime

password=3323

num=int(input('Enter The Password :- '))
deposite=0
withdrow=0
if num==password:

    while True:

      print('WElCOME IN SP BANK.. ')

      print(""" 
      1.For Know Your Balance
      2.For Add Deposite
      3.For Withdrow
      4.FOr MINI Satement
      5.For Exit
       """)
      inp1=int(input('Enter The Number :- '))

      if inp1==1:
        print('TOtal Balance :- ',deposite-withdrow)
      elif inp1==2:
        depo=int(input('Enter Amount :- '))
        deposite+=depo
      elif inp1==3:
        wit=int(input('Enter Amount : -'))
        withdrow+=wit

      elif inp1==4:
        print(datetime.now())
        print('Total Deposite :- ',deposite)
        print('Total Withdrew :- ',withdrow)
      else:
        break  




else:
    print('Invalid Password')    