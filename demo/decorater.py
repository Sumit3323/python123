
# Decorater in Python

def message(fun):
    def message2():
        print('HEllO')
        fun()
        print('How are you !')
    return message2

@message
def new_message():
    print('Good Morning')
new_message()            

# ...........................

def string1(st):
   string= st('My Name Is Sumit')
   return string


@string1
def upper1(text):
    return text.upper()

print(upper1)        


@string1
def lower(text):
    return text.lower()

print(lower)    
