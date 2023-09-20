import pandas as pd 

obj={
    'Name':['Sumit','Mehul','Ravi'],
    'Course':['Python','Javascript','Html'],
    'City':['Patan','Deesa','Delhi']
}

cd=pd.DataFrame(obj)
cd.to_csv('python/pnd1.csv')

# print(cd)
# print(cd.columns)
# print(cd.tail(1))
# print(cd.head(1))

df=pd.read_csv('python/pnd1.csv')
# df['Name'][2]='Rahul'
# df['Age']=pd.Series(10,index=[0,1,2])
# print(df)

# del df['Name']
# print(df)
# ft=df.drop(1)
# print(ft)


# abcd=df.copy()
# print(abcd)

# print(df.loc[1])


abcd=pd.Series(['Pooja','Sumit','Mehul'],index=[1,2,3])

# print(abcd)

abc=[{'a':1,'b':3},{'a':7,'b':8}]
cd=pd.DataFrame(abc,index=['read1','read2'],columns=['a','b'],)
# print(cd)

awe={'one':pd.Series([1,2,3],index=[1,2,3],),'Two':pd.Series([4,5,6],index=[1,2,3])}
dtt=pd.DataFrame(awe)
print(dtt)
