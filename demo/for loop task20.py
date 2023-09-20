str='Be Stronger Than Your Excues'

Vovels='aeiouAEIOU'

c=''


for i in str:
    for j in Vovels:
        if j in i:
            c+=i
    else:
            c+=' '    


print(c)



            