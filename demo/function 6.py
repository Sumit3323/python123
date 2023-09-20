


def f(a,b):
   

    for i in range(len(a)):
        print(i)
        if i==b:
            a.remove(a[i])
            return a        
      

Answer=f(['vikash','Hitesh','Mahesh','Pankaj'],3)
print(Answer)