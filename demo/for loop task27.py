

lis=[['sumit',55,67,89],['Hitesh',88,'98',76],['raj',55,'89']]


Number=0
str1=0


for i in lis:
    for j in i:
        if type(j)==str:
            str1+=1
        if type(j)==int:
            Number+=1

print(Number)
print(str1)                

