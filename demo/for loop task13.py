list=[11,22,33,44,55,66,77]

print('''

1.For Delete And Get Any Value
2.For Count Any Value
3.For Add New Value
4.For Add New Value Of Any Index
5.For Find Index
''')

inp=int(input('Enter Number :- '))

if inp==1:
    inp1=int(input('Enter Delete Number :- '))
    if inp1 in list:
        list.remove(inp1)
        print(list) 

if inp ==2:
    inp1=int(input('Enter Count Value :-'))
    list.count(inp1)
    print(list)

if inp ==3:
    inp1=int(input('Enter Add New NUmber :- '))
    list.append(inp1)
    print(list)
if inp ==4:
    inp1=int(input('Enter Add value  :- '))
    inp2=int(input('Enter Index :- '))

    list.insert(inp2,inp1)
    print(list)
if inp==5:
    inp1=int(input('Enter Find Index :- '))
    list1=list.index(inp1)
    print(list1)            