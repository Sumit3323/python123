import time
t=time.strftime('%x. %H.%M.%S.%p.')
print(t)
hour=int(time.strftime('%H'))
# hour=int(input('Enter Hour : '))
# print(hour)

if (hour>=0 and hour<12):
    print('Good Morning')
elif (hour>=12 and hour<18):
    print('Good Afternoon')
elif (hour>=18 and hour<0):
    print('Good Night')    
