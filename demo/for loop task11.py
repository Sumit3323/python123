obj={
        'office':'Webilok It Services',
        'Employee':{
            'vikash':7000,
            'mayank':13000,
            'hitesh':5000,
            'pankaj':19000
        },
        'Students':{
            'python':20,
            'Laravel':10,
            'PHP':5,
            'JAVA':22
        }

    }

obj2={
        
        'Total_Courses':0,
        'Total_Employee':0,
        'Total_salary':0,
        'Total_Students':0
    }



for i,j in obj['Employee'].items():
    obj2['Total_Employee']+=1
    obj2['Total_salary']+=j

for i in obj['Students']:
    obj2['Total_Students']+=1
    obj2['Total_Courses']+=obj['Students'][i]

# f=open('python/file_io.txt3','w')

# f.write((f'{obj2}'))
print(obj2)        