


inp=int(input('Enter The Value :- '))

class circle:

    def cls1(self):
        return f' circle d {self.d} circle cube {self.cube} and circle {self.c} and circle cube {self.cube2}'
   

store=circle()

store.d=inp*2
store.cube=(inp*2)**3
store.c=3.14*inp*inp
store.cube2=(3.14*inp*inp)**3


print(store.cls1())




