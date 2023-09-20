a= 'JAVA34 PHP0 C++910 LOGO7 PYTHON20 LARAVEL11 SWIFT10 PACAL70'
c=a.split(' ')
print(c)

d=''


for i in c:
    if i.endswith('0'):
        d+=i.replace('0',' ')


print(d)        


