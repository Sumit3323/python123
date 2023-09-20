
import random


arr='1234567890'


str=''
for i in range(4):
    # print(i)
    str+=random.choice(arr)


print(str)

