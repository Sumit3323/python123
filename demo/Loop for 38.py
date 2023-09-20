obj={
        'focus':'yes',
        'Dedication':'yes',
        'Excuses':'no',
        'lazy':'no',
        'kawduwgesv':'yes'
    }
c={
        'Yes':[],
        'No':[]
    }
    
   
for i in obj:
    if obj[i]=='yes':
        c['Yes'].append(i)
    if obj[i]=='no':
        c['No'].append(i)    
print(c)        

