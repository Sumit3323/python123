

subjects=['Maths','Science','English']

dic={}

for i in subjects:
    inp=float(input(f'Enter The Marks {i} :- '))
    
    dic[i]=inp

total=sum(dic.values())
per=total/len(dic)


if per<=100 :

    if per>=90:
        grade='A+'

    elif per>=80:
        grade='A'

    elif per>=65:
        grade='B'
    elif per>=50:
        grade='C'
    elif per>=33:
        grade='D'
    else:
        grade='Fail'

else:
    grade='In Valid Percentage'

  

print('-----------------------Marksheet----------------------------')

print('Subject\t\t\tMarks Obtained')

print('-'*60)

for i,j in dic.items():
    print(f'{i}\t\t\t{j}')

print('-'*60)
print(f'Total Marks :- {total}\nPercentage :- {per}\nGrade :- {grade}')
print('-'*60)


 
