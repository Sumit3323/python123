

student={
    'Name':'Sumit',
    "Surname":'Prajapati',
    'Std':12,
    'college':lambda :print('You Study In B.A'),
    'course':{
        'Python':'Yes',
        'Javascript':'NO',
        'Hacking':lambda : print('Haam KO Nahi Atta hai Ree baba')

    }
}

student['course']['Hacking']()
# print(student)
