

arr = [[23, 34, 54, 22, 23, 23],
        [23, 34, 54, 66, 77,],
        [23, 44, 56, 77, 88, 23, 45,],
        [23, 34, 56, 78, 90]]
a = int(input('enter Value  :- ' ))
b = 0



for i in arr:
        for j in i:
                # print(int(j))

                if a==j:
                   b+=1
               

print((a))  
print((b)) 
     

#  task too


# arr1 = [[23, 34, 54, 22, 23, 23],
#         [23, 34, 54, 66, 77,],
#         [23, 44, 56, 77, 88, 23, 45,],
#         [23, 34, 56, 78, 90]]

# even=[]
# odd=[]
# for i in arr1:
#         for j in i:
#                 # print(int(j))

#                 if j%2==0:
#                         even.append(j)
#                 else:
#                         odd.append(j)           


  
# print(even)
# print(odd)          