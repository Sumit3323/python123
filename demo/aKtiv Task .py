

# Task 1. Max Number ;

# l=[1,2,3,4,5,55,33,99]

# k=l[0]


# for i in l:
#     if k <=i:
#         k=i

# print(k)    
#     

# >>>>>>>>>>>>>>>>>>>>>>>>>
# task 2. peterrn

# for i in range(1,5):
#     for j in range(1,5-i):
#         print(' ',end='')
#     for k in range(1,i+1):
#         print('*',end=' ')
#     print()  
# 
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 
#Task 3. Number Length

# num=758699
# i=0

# while num !=0 :
#     num=int(num/10)
#     i=i+1

# print(i)    


# >>>>>>>>>>>>>>>>>>>>>>>>>>
digit=int(input('Enter Number  :-  '))

def compute(a):
    a=int(a)
    result=a+(a*11)+(a*111)+(a*1111)
    return result
    

print(compute(digit))    







