#   find sum of first n even numbers;

n=int(input('Enter The Number ;- ' ))



i=1
sum=0
count=0


while count<n:
    if (i%2)==0:
           sum=sum+i
           count=count+1
    i=i+1

print('Sum of Even Numbers :- ',sum)     
 


