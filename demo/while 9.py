

#  given number is palindrome number or not 


i=int(input('Enter The Number :- '))

x=i

sum=0

while i>0:
    sum=(sum*10)+(i%10)

    i=i//10

if x==sum :
    print('palindrom number ')

else:
    print('Not palindrom Number')