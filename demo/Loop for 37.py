student = {
        'firstname': 'Sumit',
        'lastname': 'prajapti',
        'age': 20,
        'marks': {
            'math': 95,
            'science': 97,
            'english': 92
        }

    }
total = 0
total2 = 0
obj2={

    }
    
    # {math: 95, science: 97, english: 92, Total: 284, PER: 94}


for i in student['marks']:
    total+=1
    total2+=student['marks'][i]
    obj2[i]=student['marks'][i]


obj2['Total']=total2
obj2['PER']=int(total2/total)
print(obj2)    





