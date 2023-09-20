#  __name__='__main__,

import time
tick=time.time()

def com_name(tk):
    return tk-tick


print(__name__)

if __name__=='__main__':
    while True:
        input('Enter Your Name :- ')
        print(com_name(time.time()))
