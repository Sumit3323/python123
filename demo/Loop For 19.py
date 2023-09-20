A = [[12, 20], [33, 22, 44, 55,], [12, 33, 44, 55, 66,], [50, 60, 70]]
ans = []


for i in A:
    # print((i))
    for j in i:
        ans.append(j+len(i))
        # print(j)
   
   
print(ans)
