arr=[5,66,34,22,14,30,4,12,22,45,67,6,78,23,44,22,33,]

obj={'kid':[],'teen':[],'young':[],'old':[]}
obj1={'kid':0,'teen':0,'young':0,'old':0}



for i in arr:
    if i <=10:
        obj['kid'].append(i)

        obj1['kid']+=1
        
        
    elif i>=11 and i<=20:
        obj['teen'].append(i)
        obj1['teen']+=1
    
    elif i>=21 and i<=45 :
        obj['young'].append(i)
        obj1['young']+=1
       
        
        
    else:
        obj['old'].append(i)
        obj1['old']+=1
        

print((obj1))
print(obj)
        

