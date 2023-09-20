
name='Sumit'
lang='Python'
sti='My Name is '+name+' and I am Future '+lang+' Developer'
print(sti)
print('My Name Is ',name,' and i am future ',lang,' developer')

st2='My Name is  %s and i am future %s developer'%(name,lang)
print(st2)

st3='My name is {0} and i am future {1} developer'
st_for=st3.format(name,lang)

st4=f'my name is {name} and i am future {lang} developer'
print(st4)


