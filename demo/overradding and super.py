#  overradding and Super()

class A:
    def __init__(self):
        print('This Class is D')

    def sum(self,a ,b):
        print("Hii")    

        return a+b

class B(A):

    def __init__(self):
        super().__init__()

        print('This class is c')

    def sum(self,a,b):
      
        # super().__init__()

        rea=super().sum(a,b)
        print(f'This is My Class Value is {a} and {b}')
        print('Sumit')
        aa=a*b
        return f'{aa} and {rea}'


obj=B()
print(obj.sum(10,5))