
from abc import ABC,abstractmethod

class shap(ABC):
    @abstractmethod
    def Printarea(self):
        return 0

class Rectangle(shap):
    type='Rectangle'
    sides=4


    def __init__(self):
        self.length=6
        self.breadth=7

    def Printarea(self):
        return self.length *self.breadth

rect1=Rectangle()
print(rect1.Printarea())

