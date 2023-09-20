#  find sum of digits of a given number

# i=int(input('Enter The Number :- '))

# sum=0

# while i>0:
#     sum +=i%10

#     i=i//10

# print('Sum Of digits :- ',sum)    




#  find sum of square of digits of a given number


i=int(input('Enter The Number :- '))

sum=0

while i>0:
    sum=sum+(i%10)*(i%10)
    i=i//10
print("sum :- ",sum)    

