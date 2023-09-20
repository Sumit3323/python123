val=int(input('Enter Value :-'))

    
c=[]

for i in range(1,val+1) :
    print(i)

    va=[]
    for j in range(1,10+1):

        va.append(i*j)

        
    c.append(va)
    
print(c)