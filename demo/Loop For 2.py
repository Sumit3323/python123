arry=[22,33,'Sumit',True,687,'Atul',False]
arry1=[22,33,'prajapti',True,687,'prajapati',False]




num=[]
str1=[]
bool1=[]


for i in (arry):
    if type(i)==int:
       num.append(i)
    if type (i)==str:
       str1.append(i)
    if type(i)==bool:
       bool1.append(i)

for i in arry1:
    if type(i)==int:
       num.append(i)
    if type (i)==str:
       str1.append(i)
    if type(i)==bool:
       bool1.append(i)

print(num)
print(str1)
print(bool1)


