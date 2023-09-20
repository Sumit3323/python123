

# find sum of even digit and odd digit of a given number

i=int(input('Enter The Number :- '))

sum=0
give=1


while i>0:

    d=i%10

    if i%2==0:
        sum+=d
    else:
        give*=d
    i=i//10


print('sum of digit :- ',sum,'malti of digit :- ',give)          
