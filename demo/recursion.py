
# def fun(a,b):
#     # fun(a,b)
#     print(a+b)
# fun(10,30)
# fun(49,51)    


#  Simple recursion

# def fact(n):
#     fac=1
#     for i in range(n):
        
#         fac=fac*(i+1)
#     return fac    

# print(fact(5))  
# 
# 
# 
# Function recursion
# 

# def recursion(n):

#     if n==0 or n==1:
#         return 1
#     else :
#         return n*recursion(n-1)    


# print(recursion(5))




# def re(n):

#     if n==0 or n==1:
#         return 1
#     else :
#         return n*re(n-1)    


# print(re(5))    




def recur_fibo(n):
    if n<=1:
        return n
    else: 
        return (recur_fibo(n-1)+recur_fibo(n-2))

n=int(input('How Many terms :'))

if n<=0:
    print('Plase Enter a positive integer')
else:
    for i in range(n):
        print(recur_fibo(i))    
