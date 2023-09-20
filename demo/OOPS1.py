class Employee:
    no_of_leaves=8
    pass



sumit=Employee()
atul=Employee()


sumit.name='Sumit'
sumit.salary=15000
sumit.role='instructor'

atul.name='Atul'
atul.salary=10000
atul.role='Student'

print(Employee.no_of_leaves)
print(sumit.__dict__)
Employee.no_of_leaves=9
print(Employee.no_of_leaves)

