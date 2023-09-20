

class Employee:
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    def printdel(self):
        return f'My Name Is {self.name} ,Salary is {self.salary} and Work in {self.role}'

    def __add__(self,other):
        return self.salary+other.salary

    def __mul__(self,other):
        return self.salary*other.salary

    def __truediv__(self,other):
        return self.salary/other.salary


emp1=Employee('Sumit',12000,'Python')
emp2=Employee('Sumit',1000,'Python')


print(emp1.printdel())
print(emp1+emp2)
print(emp1*emp2)
print(emp1/emp2)