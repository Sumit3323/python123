

# import time

# while True:
#     print(1)
#     time.sleep(2)



# from datetime import datetime

# def sp():
#     return datetime.now()

# print(sp())   
# 
# 

# from list import lis

# print(lis)


# import random

# random_number=random.random()*1000000
# int1=int(random_number)
# print(int1)

# import random
# att=['Sumit','Mitesh','Margedh','Mehul','Ravi','Rahul']
# arr=random.choice(att)
# print(arr)

# import calendar
# yy=2023
# mm=8
# print(calendar.month(yy,mm))


# import random

# # int1=random.randint(0,10)
# # print(int1)


# arr=[2,3,4,6,7,8,9]

# random.shuffle(arr)
# print(arr)


# import time 
# time.sleep(2)
# print('Sumit') 



import time
tick=time.time()

for i in range(10):
    time.sleep(.50)
    print(i)

end=time.time()-tick  
print(end)


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

i=0

while i<=10:
    print(i)
    i+=1

end=time.time()-tick  
print(end)    

    