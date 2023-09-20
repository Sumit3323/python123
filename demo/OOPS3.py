
class Employee:
     no_of_leaves=12

     def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
     def printdetails(self):
        return f'Name is {self.name}. Salary is {self.salary} and role is {self.role}'


   



add=Employee('Sumit',15000,'Instructor')
add1=Employee('sp',10000,'Student')
print(add1.__dict__)
print(add1.printdetails()) 

print(add.no_of_leaves)
Employee.no_of_leaves=10
print(add1.no_of_leaves)
    