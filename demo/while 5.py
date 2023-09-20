i=int(input('Enter The Number :- '))

org=i
sum=0

while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10

if org==sum:
    print('Number is Armstong')
else:
    print('Number is not Armstong')        