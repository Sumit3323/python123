
class con:

    def __init__(self,name,surname,Birth_year):
        self.name=name
        self.surname=surname
        self.birth=Birth_year

    def YEAR(self,year):
        self.year=year

    def print_details(self):
        # aa=self.YEAR(2023)
        ans=self.year-self.birth

        print(ans)




obj=con('sumit','prajapati',2003)

obj.YEAR(2023)
obj.print_details()



            