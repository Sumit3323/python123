arr = [['vikash', 77, 45, 43, 88], ['sumit', 23, 44, 55, 66], ['Hardik', 11, 22, 33, 44]]

s= ''
n= 0


for i in arr:
    for j in i:
        if type(j)==str:
            s+=j
            s+=' '


        if type(j)==int:
            n+=j    

print(s)
print(n)            