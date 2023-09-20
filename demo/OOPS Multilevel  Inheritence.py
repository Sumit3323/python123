# Multi level Inheritence

# class Grandfather:

#     cricket=5
# class Father(Grandfather):
#     cricket=9

#     dance=1
#     def isdance(self):
#         return f"Father Dance is {self.dance} Times"


# class Son(Father):
#     dance=9
#     def isdance(self):

#         return f"I Dance is {self.dance} Times"



# sumit=Son()

# print(sumit.dance)



# Example 2


class Employee:
    number=1
    name='Xyz'

class salary(Employee):
    salary=1500


class role(salary):
    role='Python'

class total(role):

    def sp(self):
        return f'My id is {self.number}\nName Is {self.name}\nSalary id {self.salary}\nRole {self.role}'




sumit=total()

print(sumit.sp())





