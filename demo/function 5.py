


lis=[]
def cheklist(a,b):
    for i in b:
        p=(len(i))

        if p>a:
            lis.append(i)
    return lis    

    
An=cheklist(6,['success','Not','journey','vikash','ok','defind'])
print(An)    