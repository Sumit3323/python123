def greet(fx):
    def mfx(*args,**kwargs):
        print('Good Morning')
        fx(*args,**kwargs)
        print('Thanks For Using This Function')
    return mfx

@greet
def hello():
    print('Hello World')

hello()    
@greet
def add(a,b):
    print(a+b)
add(2,3)


