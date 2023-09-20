set1={1,2,3,4,5,6,7,8,9}

# print(set1)

# set2=set()
set1.add(10)
# set2.add(50)
# set2.add('Sumit')
# set2.add(33)
print(set1)


a={11,22,33,44,55,66,77,88,99,24,34,56}
b={12,34,56,33,55,99,2,3,11,22}
c=a.intersection(b)
# d=b.intersection(a)
# print(d)
print(c)



# a.update(b)
b.update(a)
print(b)



city1={'patan','Deesa',}
city2={'patan','Deesa','Delhi',}

city3=city1.intersection(city2)
# print(city3)
city2.intersection_update(city1)
# city3=city1.symmetric_difference(city2)
# city1.symmetric_difference_update(city2)

print(city2)
# print(city1.isdisjoint(city2))  value is not same is true
print(city1.issuperset(city2))
print(city1.issubset(city2))

