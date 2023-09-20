


class ListProcessor:
    def __init__(self):
        self.list1=[100,200,300,400,500]
        self.list2=[]

    def Processor_list(self):
        while True:
            if not self.list1:
                break

            inp=int(input('Enter Any Number : '))

            if inp in self.list1:
                self.list1.remove(inp)
                self.list2.append(inp)

                print('list1 : ',self.list1)    
                print('list2 : ',self.list2)

            elif inp in self.list2:
                print('This Number is Already Added in List2')
            else:
                print('This Number is Not Available')            


processor=ListProcessor()

processor.Processor_list()





# class fun:

#     def __init__(self,lis):

#         self.lis=lis
#         self.list1=[]

#     def print_details(self):

#         for i in range(len(self.lis)):
#             inp=int(input('Enter The Value :- '))

           
#             if inp  in self.lis:
#                  self.lis.remove(j)
#                  self.list1.append(j)

#             print(self.lis)
#             print(self.list1)        
           

# op=[100,200,300,400,500]

# sp=fun(op)

# sp.print_details()