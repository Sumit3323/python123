


lis=[]
set1=set()
def make(a):

    for i in a:
        set1.add(i)
    for j in set1:
        lis.append(j)
    return lis        

print(make([22,33,44,22,33,45,45.11,90]))    