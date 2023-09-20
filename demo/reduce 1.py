
from functools import reduce



# def lis2(a,b):
#     return a+b

# lis=[1,2,3,4,5,6,7,8,9,10]

# print(reduce(lis2,lis))



lis=[1,2,3,4,5,6,7,8,9,10]

print(reduce(lambda a,b:a+b,lis))


