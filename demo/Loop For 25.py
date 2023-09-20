a = Number=int(input('Which NUmber"s multipales U Want?? :- '))
b = Number1=int(input('Enter Your Limit :- '))


su = 0

odd = []
even = []
sq = []
cub = []

for i in range(a,b+1):
    # if i%2==0:
    #   even.append(i)
        if (i % a == 0) :
            print(i,end=' ') 
            # print(sum(i))
            su+=i
             

            sq.append(i * i)
            cub.append(i * i * i)

            if (i % 2 == 0) :
                    even.append(i)
                
            if (i % 2 != 0) :
                    odd.append(i)


print('\n sum :- ',su)
print('square :- ',sq)
print( 'Cube :- ',cub)
print('even Numbers :- ',even)
print('Odd Numbers :- ',odd)