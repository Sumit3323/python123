sr= 'Be Stronger Than Your Strongest Excuse Ahjx ahdixgasjz'
# i = 0

even = ''
odd = ''


for i in range(len(sr)):
    # print(i-1)
    if i!=' ':
        if i%2==0:
            even+=sr[i]
        else:
            odd+=sr[i]
   
print('Even Number :- ',even)
print("odd Number :- ",odd)
               
