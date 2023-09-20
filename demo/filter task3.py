arr=[1,2,3,4,5,6,7,8,9,12,14,15,16,14,12,10,22,33,44,55,66,77]





def even(a):
    return a%2==0

# def square(b):
#     return b**2


# is_even=list(filter(even,arr))
# square=list(map(square,is_even))

# print(is_even)
# print(square)    





# def fun(a):
#     return a%2==0

# c=list(filter(fun,arr))
# print(c) 

# print(list(map(lambda a:a**3,arr)))
v=[i**3 for i in arr if i>10 ]
print(v)

d=list(filter(lambda a:a>10,arr))
# print(d)

# even number :
c=list(filter(lambda a : True if a%2==0  else False,arr))
print(c) 


# cube and square

square=list(map(lambda a:a**2,arr))
# print(square)

cube=list(map(lambda a:a**3,arr))
# print(cube)



