
class obj:

    def __init__(self,name,sname,std,clg,course):
        self.name=name
        self.surname=sname 
        self.std=std
        self.college=clg 
        self.course=course



store=obj('Sumit','Prajapati',12,lambda :print('You Study In B.A'),{'Python':'Yes','Javascript':'No','Hacking':lambda :print('Haam Ko Nahi atta Hai Ree Baba')})

store.course['Hacking']()
store.college()