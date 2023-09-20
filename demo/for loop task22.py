
dic={}
while True:

    print('''
    
    1.For Add New Ky & Value
    2.For Show Dictonery
    3.For Serch Key
    4.For Delete Key
    5.For Change Value
    6.For Exit

    ''')

    inp=int(input('Enter The Value :- '))


    if inp==1:
        key=input('Enter key ":- ')
        value=input('Enter Value : - ')
        dic[key]=value
    elif inp==2:
        print(dic)
    elif inp==3:
        serch=input('Enter Serch Key :- ')
        print(dic[serch]) 
    elif inp==4:
        delete=input('Enter Delete Key :- ')
        del dic[delete]
    elif inp==5:
        inp2=input('Enter Change Key : -')
        inp3=input('Enter Change Value : - ')
        dic[inp2]=inp3
    else:
        break


