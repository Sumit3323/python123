st=input('Enter The Value :- ')

upper=0
loweer=0
num=0
sp=0
space=0


for i in st:

    if  i.isupper() :  #(i>='A') and (i<='Z'):
        upper+=1
    elif i.islower(): #(i>='a') and (i<='z'):
        loweer+=1
    elif i.isdigit():     #(i>='0') and (i<='9'):
        num+=1
    elif i.isspace():
        space+=1
    else:
        sp+=1


print('UPPER CASE :- ',upper)
print('LOWER CASE :- ',loweer)
print('NUMBER :- ',num)
print('space :- ',space)
print('Special :- ',sp)                    

            