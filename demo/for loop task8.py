

name='MY NAME IS SUMIT'

cap='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sma='abcdefghijklmnopqrstuvwxyz'


nam=''

for i in range(len(name)):

    if name[i] != ' ':
        if i %2 !=0:
            cap1=cap.index(name[i])
            small=sma[cap1]
            nam+=small
        else:
            nam+=name[i]

    else:
        nam+=' ' 

print(nam)                   



  