
# pettern 1 for loop

# for i in range(1,10+1):

#     # print(i+1)
#     for j in range(1,i+1):
#         print(j,end='')

#     print('')    





# pettren 2 for loop


# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()        



#  pettren 3 for loop

# for i in range(1,5+1):
#     for j in range(1,(5+1)-i):
#         print(' ',end='')
#     for k in range(1,i+1):
#         print('*',end='')
#     print()        

# pettren 4 


# for i in range(1,5+1):
#     for b in range(1,(5+1)-i):
#         print(' ',end='')
#     for k in range(1,i+1):
#         print('*',end=' ')
#     print()        



# pettern 5


# for i in range(4,0,-1):
#     for j in range(0,(4+1)-i):
#         print(' ',end='')
#     for k in range(1,i+1):
#         print('*',end=' ')
#     print()        


 

#   pettern 6

# row=5
# k=2*row-2

# for i in range(0,row):
#     for j in range(0,k):
#         print(end=' ')
#     k=k-1
#     for j in range(0,i+1):
#         print("*",end=' ')
#     print()    

# k=row-2

# for i in range(row,-1,-1):
#     for j in range(k,0,-1):
#         print(end=' ')

#     k=k+1
#     for j in range(0,i+1):
#         print('*',end=' ')
#     print()    




# >>>>>>>>>>>>>>>>

row=5

for i in range (0,row):
    for i in range(0,i+1):
        print('* ',end=' ')
    print('')    

for i in range (row,0,-1):
    for i in range(0,i-1):
        print('* ',end=' ')
    print('')    







    






