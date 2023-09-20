#  find sum of square from 1 to n
n=int(input('Enter Number :- '))

sum=0

i=1

while i<=n:
    sum=sum+i*i

    i=i+1

print('Sum :-',sum)    


# For loop

c=0
for i in range(1,n+1):
    c+=i*i

print('sum :',c)    
