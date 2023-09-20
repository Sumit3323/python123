list=[100,200,300,400,500,600]


list1=[]



while True:

    inp=int(input('Enter Any NUmber :- '))

    if inp in list:

        list1.append(inp)
        list.remove(inp)
        print(list)
        print(list1)
    elif inp in list1:
        print('This Number Is Already Added In Newlist') 
    else:
        print('This Number Is Not Avalible')       
  