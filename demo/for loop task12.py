Points_Table={
    'India':10,
    'Pakistan':8,
    'South Africa':6,
    'Bangladesh':2,
    'Aus':4
}


inp=input('Enter Country Name :- ')

for i,j in Points_Table.items():
   
   if inp ==i:
    print(f'{i} has Got {j} Points')
 
