

class Person:

    def __init__(self,name):
        self.name=name

class Student(Person): 
    def __init__(self,roll,name):
        super().__init__(name)       
        self.roll=roll
        self.dict={}

    def Add_mark(self,sub,marks):
        self.dict[sub]=marks


    def total_marks(self):
       return sum(self.dict.values())

    def get_average_mark(self):
        total=self.total_marks()
        sub=float(total/len(self.dict))
        return sub

class Marksheet(Student):
    def print_details(self):
        print('Roll Number :- ',self.roll)
        print('Name :- ',self.name)
        print('Marksheet :- ')

        for i,j in self.dict.items():
            print(f'{i} : {j}')

        print('Total Mark :- ',self.total_marks())
        print('Average Marks :- ',self.get_average_mark())
   


sumit=Marksheet(33,'Sumit')
rahul=Marksheet(46,'rahul')

sumit.Add_mark('Math',90)
sumit.Add_mark('sci',85)
sumit.Add_mark('Hindi',78)

rahul.Add_mark('Math',75)
rahul.Add_mark('Sci',88)
rahul.Add_mark('Hindi',92)



print('Student Marksheet :')
print('-'*50)
sumit.print_details()
print('-'*50)
rahul.print_details()
print('-'*50)

     

   

# class sp:

#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll
#         self.dict={}

#     def  mark(self,sub,marks):
#         self.dict[sub]=marks


#     def total_mark(self):
#        return sum(self.dict.values())

#     def avarage(self):
#         total=self.total_mark()
#         sub=float(total/len(self.dict))
#         return sub

#     def print_details(self):
#         print('Roll Number :- ',self.roll)
#         print('Name :- ',self.name)
#         print('Marksheet :- ')

#         for i,j in self.dict.items():
#             print(f'{i} : {j}')

#         print('Average Marks :- ',self.avarage())
#         print('Total Mark :- ',self.total_mark())
   


# s=sp('Sumit',33)
# p=sp('SP',99)

# s.mark('Math',90)
# s.mark('sci',85)
# s.mark('Hindi',78)

# p.mark('Math',75)
# p.mark('Sci',88)
# p.mark('Hindi',92)



# print('Student Marksheet :')
# print('-'*50)
# s.print_details()
# print('-'*50)
# p.print_details()
# print('-'*50)

     

   



