
class Employee:
    no_of_leaves=8
    

    def printdetails(self):
        return f'Name is {self.name}. Salary is {self.salary} and role is {self.role}'



sumit=Employee()
atul=Employee()


sumit.name='Sumit'
sumit.salary=15000
sumit.role='instructor'

atul.name='Atul'
atul.salary=10000
atul.role='Student'


print(sumit.printdetails())