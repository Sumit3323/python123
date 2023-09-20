arr = ['php', 'laravel', 'python', 'sql', 'vikash']

even = []
odd = []




for i in range(len(arr)):
    
    if i%2==0:
        even.append(arr[i])
    else:
        odd.append(arr[i])

print(even)
print(odd)            

