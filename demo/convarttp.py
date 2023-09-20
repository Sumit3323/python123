

# Temperature Converter
# def fun(a1):

#  sp=inp.split(' ')

#  if sp[1]=='C':
#     print((float(sp[0])*9/5)+32)
#  elif sp[1]=='F':
#     print((float(sp[0])-32)*5/9)

# inp=input('Enter Temperature C/F :- ').upper()

# fun(inp)




# Replace Worlds Form Dictionary


# def dic(dic):
#     inp=input('Enter The World :- ')
#     sp=inp.split(' ')

#     store=''

#     for i in sp:
       
#        if i=='Computer':
#         store+=i.replace(i,dic['Computer'])
#         store+=' '
#        elif i=='Education':
#         store+=i.replace(i,dic['Education'])
#         store+=' '
#        else:
#         store+=i
#         store+=' '

#     print(store)      
        
      
# dict1 ={
#     'Computer':'Softwere',
#     'Education':'Solution'

# }

# dic(dict1)  






# Create Mixed Sting


def Mixed_string(str1,str2):

    sp=str2[::-1]
    store=''

    for i in range(len(str1)):
        store+=str1[i]
        store+=sp[i]
    print(store)    




s1='ABC'
s2='XYZ'

Mixed_string(s1,s2)






s1 = "Aktiv"
s2 = "Software"
output = ""

sp=s2[::-1]

# len1=len(s1)
# len2=len(sp)

max_len = max(len(s1), len(sp))
print(max_len)


for i in range(max_len):

    if i < len(s1):
        output += s1[i]
    if i < len(sp):
        output += sp[i]


print(output)
