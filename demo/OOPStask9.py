

class lis:

    def __init__(self,list1):
        self.list=list1
        self.list2={}


    def square(self):
        for i in self.list:
            self.list2[i]=i*i
        return f'Squared Dictionary :- {self.list2}'


    def cube(self):
        for i in self.list:
            self.list2[i]=i*i*i
        return f'Cube Dictionary :- {self.list2}'



Input_numbers=[2,3,4,5,6]

sp=lis(Input_numbers)

print(sp.square())
print(sp.cube())


        
                            