

n=int(input('Enter The Number :- '))

dic={}
def make(aa):

    for i in range(1,n+1):
        dic[i]=i**3
    return dic   
        

print(make(n))    