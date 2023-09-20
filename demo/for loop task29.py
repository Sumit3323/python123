

str='a9 b3 m5 k2 h2 s4'
# str1=str.split(' ')


m=''
for i in str:
  

    if i != ' ':
        # print(i)
        if i.isalpha():
            c=i
        if i.isdigit():
            d=int(i)
            m+=c*d 
    else:

        m+=' '  
                
print(m) 
          
  




        

   







    

