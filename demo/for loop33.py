
x=[10,20,340,47]
y=[10,150,20,30,40,50]
z=[10,270,30,30,470,270]


while True:

    inp=int(input('Enter The Number : - '))

    def num():
    
      for i in x:
         for j in y:
            for k in z:
                if i+j+k==inp:
                    return i,j,k
    


    print(num())        



