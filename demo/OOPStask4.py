

class obj:

    def __init__(self,maths,hindi,guj,sci,ss,per,total,result):
        self.maths=maths
        self.hindi=hindi
        self.guj=guj
        self.sci=sci
        self.ss=ss
        self.per=per
        self.total=total
        self.result=result


store=obj(90,56,34,78,56,'','','')


store.total=store.maths+store.guj+store.hindi+store.sci+store.ss

store.per=store.total/5

if store.per <=100:
    if store.per>=33:
        store.result='Pass'
    else:
        store.result='Fail'    
else:
    store.result='Invalid Per'

print(store.__dict__)