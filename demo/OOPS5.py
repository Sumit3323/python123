class MobilePhone:

    made_in='INDIA'

    def __init__(self,model,price):

        self.smodel=model
        self.sprice=price

    @classmethod
    def Change_made_in(cls,value):
        cls.made_in=value

    @classmethod
    def Change_value(cls,String):
        return cls(*String.split('-'))

    @staticmethod
    def Printproog(str):
        return f'This Name  Is {str}'    

Apple=MobilePhone('IPhone 12',120000)
OPPO=MobilePhone.Change_value('F19PRO+ - 23000')
#   
print(Apple.made_in)
Apple.Change_made_in('IND')
print(Apple.made_in)
print(OPPO.__dict__)

print(Apple.Printproog('Sumit'))