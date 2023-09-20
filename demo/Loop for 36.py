obj={
        'Name':'Sumit',
        'Lastname':'prajapati',
        'Gender':'male',
        'Study':'B.A',
        'Age':20
    }
a=[]   #key
b=[] #value



for i in obj:
    # a.append(obj)
    a.append(i)
    b.append(obj[i])


print(a)
print(b)