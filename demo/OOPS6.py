
#  OOPS Inheritance


class Employee:

    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    def print_details(self):
        return f'Your Employee Name Is {self.name} ,Salary is {self.salary} and Worl in {self.role}'    



class Programmer(Employee):
    def __init__(self,name,salary,role,language):
        self.name=name
        self.salary=salary
        self.role=role
        self.language=language


    def printproog(self):
        return f' Your Programer Name is {self.name} ,Salary is {self.salary} and work in {self.role} Company Likes Language {self.language}'    


    







sumit=Employee('Sumit',50000,'Python')
Mitesh=Programmer('Mitesh',60000,'Javascript',['Javascript','HTML'])        

print(Mitesh.printproog())