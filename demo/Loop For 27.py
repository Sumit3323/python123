arr2=['100%','250$','300%','500$']
newarr=[]


for i in arr2:
    if i.endswith('%'):
        newarr.append(i.replace('%',' '))
    if i.endswith('$'):
        newarr.append(i.replace('$',' '))    
print(newarr)
