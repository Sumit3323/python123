

password='knjd@@8H'

obj={
        
        'sma':0,
        'specialchar':0,
        "cap":0,
        'num':0

    }

for i in password:
    # print(i)
        if i>='A'and i<='Z':
            obj['cap']+=1

        elif i>='a'and i<='z':
            obj['sma']+=1

        elif i>='0' and i<='9' :
            obj['num']+=1
        else:
            obj['specialchar']+=1    
    
    
print(obj)
# print(len.password)
obj['total']=obj['cap']+obj['sma']+obj['num']+obj['specialchar']
print(obj)

if obj['total']>= 6 and obj['total']<=12:
     if obj['cap']==0 or obj['sma']==0 or obj['num']==0 or obj['specialchar']==0:
        print('invalid password')
     else:
        print('valid paswword')    
else:
    print('invalid password')




