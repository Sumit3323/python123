arr=[1,2,3,4,5,6,7,8,9]

def num(aa):
    return aa>5

grater=list(filter(num,arr))
print(grater)    