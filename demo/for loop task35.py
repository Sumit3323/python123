

str2='drem plans action reality stronger drem'

str1=str2.split(' ')

sp=[]

for i in (str1):
    # st=str(len(i))
    # print(st)
    sp.append(str(len(i))+i)
    sp.sort()

print(sp)    
    