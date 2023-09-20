
lis=[]
c=''
for i in range(1,4):
    dic={}
    print(f' Round {i} ')
    name=input('Enter The Name :- ')
    maths=int(input('Enter The Maths Marks :- '))
    sci=int(input('Enter The Sci Marks :- '))
    eng=int(input('Enter The English Marks :- '))

    dic['Name']=name
    dic['Maths']=maths
    dic['Sci']=sci
    dic['English']=eng

    total=maths+sci+eng
    dic['Total']=total

    lis.append(dic)
    c+=(f"Name: {name} , Total Marks : {total}\n")


print(lis)    
print(c)
