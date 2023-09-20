

dict={
    'office':'webilok',
    'python':{
        'Fee':50000,
        'students':['Rahul 50000','nilesh 18000','Hitesh 50000','pankaj 25000']
    }

}
st=''
for i in dict['python']['students']:

    store=(i.split())
    
    if int(store[1])==dict['python']['Fee']:
        print(f'{store[0]} Your Total Fee Paid')
    else:
        fee=int(store[1])-dict['python']['Fee']
        print(f"{store[0]} baki Fee = {fee} out of {dict['python']['Fee']} ")    
    
    
    
    