class Employee:
    # _name='xyz'
    _Projected='Pythod'  # Protected With _(singel Underscore)
    __sumit='Sumit'#Private With __(Double Underscore)


    def __init__(self,name,salary,role):

        self.name=name
        self.salary=salary  #Public Attibute
        self.role=role

    def printdetails(self):
        return f'Your Employee Name Is {self.name} , Salary is {self.salary} and Work in {self.role}'    


sp=Employee('Sumit',50000,'Python')

print(sp.printdetails())
print(sp._Employee__sumit)
