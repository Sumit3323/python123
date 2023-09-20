


#  reverse a given number 


i=int(input('Enter The Number :- '))

# x=i

sum=0

while i>0:
    sum=(sum*10)+(i%10)

    i=i//10


print(sum)




