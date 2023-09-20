

up=0
left=0


while True:
   
    
    inp=(input('Enter The Steps :- '))

    sp=inp.split(',')

    if sp[0]=='up':
        up+=int(sp[1])
    elif sp[0]=='down':
        up+=int(sp[1])
    elif sp[0]=='left':
        left+=int(sp[1])
    elif sp[0]=='right':
        left+=int(sp[1])
    elif inp=='close':
        f=open('python/file_io 1.txt','a')
        f.write((f'\nup site steps {up} left site steps {left}'))

        break    