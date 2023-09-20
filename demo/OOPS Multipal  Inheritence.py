
class Employee:

    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    def Printdetails(self):
        return f'Your Employee Name is {self.name} , salary is {self.salary} and work in {self.role} Company'

class Player:

    def __init__(self,name,game):
        self.name=name
        self.game=game

    def Printfdetails(self):
        return f'Your Player Name is {self.name} ,ame paly {self.game}'

class son(Player,Employee):
    pass


sumit=Employee('sumit',10000,'python')
mitesh=Employee('mitesh',19000,'html')
rahul=Player('rahul','Free-fire')
mp=son('rahul','Free-fire',)

print(mp.Printdetails())