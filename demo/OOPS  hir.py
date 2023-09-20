
class Family:
    def family(self):
        print('This is My Family')

class Father (Family):
    Father_name=''

class Mother(Family):
    Mother_name=''

class son(Mother,Father) :

    def total(self):
        print(f'My Father Name IS {self.Father_name} And My Mother Name Is {self.Mother_name}')       



sp=son()

sp.Father_name='PrahladBhai'
sp.Mother_name='Madhuben'

sp.total()
print(sp.__dict__)
sp.family()