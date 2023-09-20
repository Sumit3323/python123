

class Employee:
     no_of_leaves=12

     def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

     def printdetails(self):
        return f'Name is {self.name}. Salary is {self.salary} and role is {self.role}'

     @classmethod
     def chang_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
     
     @classmethod

     def from_str(cls,string):
      #   params=string.split('-')
      #   return cls(params[0],params[1],params[2])
        return cls(*string.split('-'))

          

add=Employee('Sumit',15000,'Instructor')
add1=Employee('sp',10000,'Student')
add2=Employee.from_str('Karan-480-students')

print(add2.__dict__)


add.chang_leaves(34)
print(add2.no_of_leaves)
# print(add.__dict__)
# print(add1.printdetails()) 

# Employee.no_of_leaves=10
# print(add1.no_of_leaves)
# print(add.no_of_leaves)