num='19.99'

spl=num.split('.')

ans=''

if spl[1] >='50':
    ans=int(spl[0])+1
else:
    ans=spl[0]    
print(ans)    

