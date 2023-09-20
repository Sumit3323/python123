
class obj:

    def __init__(self,Office,Employee,Students):
        self.Office=Office
        self.Employee=Employee
        self.Students=Students



store=obj('Webilok It Services',{'Vikash':10000,'Mayank':5000,'Hitesh':15000,'Pankaj':20000},{'Python':20,'Laravel':10,'PHP':5,'Java':12,'Go':15})


print(store.__dict__)

Total_Employee=0
Total_Salary=0
Total_Students=0
Total_Courses=0

for i in store.Employee:
    Total_Employee+=1
    Total_Salary+=store.Employee[i]

for i in store.Students:
    Total_Students+=1
    Total_Courses+=store.Students[i]

print(f'Total_Employee : {Total_Employee}\nTotal_Salary : {Total_Salary}\nTotal_Students : {Total_Students}\nTotal_Courses : {Total_Courses}')        