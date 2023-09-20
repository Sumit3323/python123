dic={
    'Name':'Sumit',
    'Surname':'Prajapati',
    'Std':12,
    'Age':20
}


# print(dic)
# inp=input('Enter The Value :- ')
# print(dic[inp])

# dic['Name']='Rahul'
dic['cource']='Python'

# dic.update({'cource':'html'})
dic.update({'Village':'Delvada'})
del dic['cource']
print(dic.keys())
print(dic.values())
print(dic.items())
print(dic.get('Age'))
print(dic['Name'])

print(dic)






d1={'sumit':"Burger",
"rohan":'pakodi',
'atul':'name',
'rajesh':{
    'age':20,'std':12
}}

d1['Ankit']='Junk food'
d1['kisan']=12


# print(d1)
# del d1['Ankit']
# print( type(d1))
# print(d1)

# print(d1['rajesh']['age'])

# print(d1.copy())
# d2=d1.copy()
# del d2['kisan']
# print(d1.get('kisan'))

# d1.update({'leena':'toffee'})
# print(d1)
# print(d1.keys())
# print(d1.items())

dic={'tee':19,'t':90}
dic2={'teen':10,'ten':60}

dict22={**dic,**dic2}
print(dict22)






