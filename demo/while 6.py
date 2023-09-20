

i=int(input('Enter The Number :- '))

prod=1


while i>0:

    prod=prod*(i%10)

    i=i//10

print('Product of digit :- ',prod)    