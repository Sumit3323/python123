
#  Not Mach lastindex
st = 'java script batch is start'
# print(st.index('a'))
y=''

for i in st:
    if st.index(i)==st.rindex(i):
       y+=i
       y+=' '
print(y)        
