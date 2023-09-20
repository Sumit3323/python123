

n=int(input('Enter The Number :- '))


c=0
for i in range(1,n+1):
    if (n%i==0):
        c+=1


if c==2:
    print('Prime Number')
else:
    print('Not Prime Number')




# count=0

# i=1

# while i<=n:
#     if (n%i==0):
#         count=count+1
#     i=i+1


# if count==2:
#    print ('Prime Number ')

# else:
#     print('Not Prime  Number ')          





    