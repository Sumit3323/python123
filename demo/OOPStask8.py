

class obj:

    def __init__(self,a,b):
        self.A=a
        self.B=b

    def print_details(self):
        self.total=self.A+self.B
        return self.total



Object=obj(20,39)
print(Object.__dict__)
print(Object.print_details())