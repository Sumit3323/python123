str='vik 15 ash 12 modi 8 okk'

str1=str.split(' ')
# print(str1)9

lis=[]

for i in str1:

    if i.isdigit():
    # if i>='0' and  i<='9' :
        lis.append(int(i))
print(lis)


        


