obj={
        'office':'Webilok',
        'python':{
            'fee':50000,
            'Students':['vikash Yes','Hitesh Yes','Pankaj No','mayank No']
        },
        'PHP':{
            'Fee':20000,
            'Students':['Rajesh Yes','vivek No','Nikhil Yes']
        },
        'JAVA':{
            'Fee':30000,
            'Students':['Hitesh Yes','Sumit Yes','Atul No']
        }
    }
obj2={
        'Yes':[],
        'No':[]
    }


for i in obj['python']['Students'] :

    spl=i.split(' ')

    if spl[1]=='Yes':
        obj2['Yes'].append(spl[0])
    if spl[1]=='No':
        obj2['No'].append(spl[0])
        

for i in obj['PHP']['Students'] :

    spl=i.split(' ')

    if spl[1]=='Yes':
        obj2['Yes'].append(spl[0])
    if spl[1]=='No':
        obj2['No'].append(spl[0])

for i in obj['JAVA']['Students'] :

    spl=i.split(' ')

    if spl[1]=='Yes':
        obj2['Yes'].append(spl[0])
    if spl[1]=='No':
        obj2['No'].append(spl[0])
                        
            

print(obj2)        



  
    
