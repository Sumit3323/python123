lis=[100,200,300,400,500,600]

lis1=[]
while True:
    inp=int(input('Enter The Value :- '))

    if inp in lis:
        lis1.append(inp)
        lis.remove(inp)
        print(lis)
        print(lis1)
    elif inp in lis1:
        print('This NumberIs AlreadyAdded In NewList ')
    else:
        print('This Number Is Not Avalible ')        
       
