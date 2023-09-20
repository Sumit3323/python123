
obj = {
        'office': 'Webilok',
        'python': ['vikash', 'sumit', 'pankaj', 'atul', 'gjg', 'uyy', 'uyhih'],
        'php': ['rajesh', 'vivek', 'nikhil'],
        'java': ['nilesh', 'hitesh', 'sunil', 'dhaval']
    }


c=0
for i in obj:
    if type(obj[i])==list:
        c+=1
print(c)        




