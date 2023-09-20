obj = {
        'office': 'Webilok',
        'python': ['vikash', 'sumit', 'pankaj', 'atul', 'gjg', 'uyy', 'uyhih'],
        'php': ['rajesh', 'vivek', 'nikhil'],
        'java': ['nilesh', 'hitesh', 'sunil', 'dhaval']
    }



python=0
php=0
java=0



for i in obj['python']:
    # print(i)
    python+=1

for i in obj['php']:
    # print(i)
    php+=1

for i in obj['java']:
    # print(i)
    java+=1    

print(python)  
print(php)
print(python)  