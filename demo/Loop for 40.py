obj={
        'office':'Webilok',
        'Employee':{
            'vikash':7000,
            'MAyank':13000,
            'hitesh':5000,
            'mukesh':19000
        },
    }

obj2={
        'Lower_Salary':[],
        'Higher_salary':[],
        'Higher_Employee':[],
        'Lower_Employee':[],
        'Lower_salary_Counting':0,
        'Higher_salary_counting':0

    }


for i in obj['Employee']:
  
    if obj['Employee'][i] <=7000:
      obj2['Lower_Salary'].append(obj['Employee'][i])
      obj2['Lower_Employee'].append(i)
      obj2['Lower_salary_Counting']+=obj['Employee'][i]

    if obj['Employee'][i]>7000:
        obj2['Higher_salary'].append(obj['Employee'][i])
        obj2['Higher_Employee'].append(i)
        obj2['Higher_salary_counting']+=obj['Employee'] [i]
print(obj2)   
