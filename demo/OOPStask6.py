

class Marksheet:

    def __init__(self,subject):
        self.sub=subject
        self.dic={}
        self.total=0
        self.per=0
        self.grade=''


    def Marks(self):
        for i in self.sub:
            inp=float(input(f'Enter Your Marks {i} :- '))
            self.dic[i]=inp

        # print(self.dic)      

    def Total_Marks(self):
        self.total=sum(self.dic.values())   
        print( f'Total_Marks :-  {self.total}') 

    def Total_per(self):
        self.per=self.total/len(self.dic)
        print( f'Total_Per :- {self.per}')

    def Grade(self):
        # self.per=self.Total_per()

        if self.per<=100 :

           if self.per>=90:
               self.grade='A+'

           elif self.per>=80:
               self.grade='A'

           elif self.per>=65:
               self.grade='B'
           elif self.per>=50:
               self.grade='C'
           elif self.per>=33:
              self.grade='D'
           else:
              self.grade='Fail'
        else:
              self.grade='Invalid Per'   

        print( f'Grade :- {self.grade}')      

    def print_Marksheet(self):

        print('-----------------------Marksheet----------------------------')

        print('Subject\t\t\tMarks Obtained')

        print('-'*60)

        for i,j in self.dic.items():
           print(f'{i}\t\t\t{j}')

        print('-'*60)

        self.Total_Marks()
        self.Total_per()
        self.Grade()

        print('-'*60)

sub=Marksheet(['Maths','English'])        

sub.Marks()
sub.print_Marksheet()
