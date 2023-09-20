

# inp=list(map(int,input('Enter The Number List ;')))

# print(inp)

# even=list(filter(lambda x:x%2==0,inp))
# odd=list(filter(lambda y:y%2!=0,inp))

# squ=list(map(lambda v:v*v,inp))
# print(squ)


# print(even)
# print(odd)





inp2=(input('Enter The Number :- ').split(','))

inp3=list(map(int,inp2))

inp4=(list(filter(lambda x :x%2==0,inp3)))
print(inp4)
print(list(map(lambda x:x**2,inp4)))



