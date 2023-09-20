#  emailid 


min='sumit123@@gma&il.com'



obj={
    'cap':0,
    'small':0,
    'num':0,
    'special':0
}

a=0
b=0

for i in min:

    if i >='A' and i<='Z':
        obj['cap']+=1
    if i >='a' and i<='z':
        obj['small']+=1
    if i >='0' and i<='9':
        obj['num']+=1
    if i=='@' or i=='.':
        obj['special']+=1
    if i=='@':
        a+=1
    if i=='.':
        b+=1


if (obj['cap']>0 or obj['small']==0 or obj['num']==0 or obj['special']==0 or  (a>1 or b>1)):
    print('Invalid Emailid')
else:
    print('Valid Emailid')            

                    
print(obj)                