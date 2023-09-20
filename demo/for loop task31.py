

str1='sumit'
ans=[]
for i in range(len(str1)):
    # print(str1[i])
    for j in range(i+1,len(str1)+1):
        print(j)
        ans.append(str1[i:j])
print(ans)        