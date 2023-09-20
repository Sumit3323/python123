

class CompenyFee:

    def __init__(self,name,Total_Fee,Paid_fee):
        self.name=name
        self.Total_Fee=Total_Fee
        self.Paid_fee=Paid_fee
        self.lis=[]

    def fees(self):
        self.total=self.Total_Fee-self.Paid_fee    

    def print_details(self):
        sp=self.fees()
        self.lis.append(f'Dear {self.name} Yout Total Fee Is {self.Total_Fee} and Paid Fee is {self.Paid_fee} Your Remaing Fee Is {self.total}')

        return self.lis


obj=CompenyFee('Sumit',30000,20000)
print(obj.print_details())          