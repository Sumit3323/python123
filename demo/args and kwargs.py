
# *args and **kwargs

arr=['Sumit','Mitesh','Margesh','Ravi','Mehul','Rahul']

def name(*args,**kwargs):
    print(args,kwargs)

dic={'Name':'Sumit','Surname':'Prajapati'}
name(*arr,**dic)
