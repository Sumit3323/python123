
str='cat matter okk Success is a Noot'
str1=str.split()

lis=[]
for i in str1:
    print(i)
    for j in i:
        print(j)
        store=i.count(j)
        
        if store >1:
            lis.append(i)


print(lis)     
