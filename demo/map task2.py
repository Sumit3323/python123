arr=['2','4','5','6','7']

aa=list(map(int,arr))

# print(aa)

ans=list(map(lambda x:x**3,aa))
print(ans)