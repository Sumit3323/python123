
str='Be Stronger Than Your Excues'

#  find Index
inp=input('Enter Your Word :- ')

for i in range(len(str)):
    if inp[0] in str[i]:
        print(i)