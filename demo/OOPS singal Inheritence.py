

class Employee:

    def __init__(self,name,salary,role):
        self.namae=name
        self.salary=salary
        self.role=role

    def Printdetails(self):
        return f'Your Employee Name is {self.name}, salary is {self.salary} and work in {self.role}'


class programmer(Employee):

    def __init__(self,name,salary,role,Language):
        self.name=name
        self.salary=salary
        self.role=role
        self.Language=Language

    def printproog(self):
        return f'Your Programmer Name Is {self.name} ,Salary is {self.salary} and work in {self.role} company,likes Language {self.Language}'



sumit=Employee('sumit',15000,'Python')
mitesh=Employee('Mitesh',2999,'Javascript')
rahul=programmer('Mitesh',2999,'Javascript',['html','css'])

print(rahul.Printdetails())
print(rahul.printproog())

