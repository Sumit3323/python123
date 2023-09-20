
import random


def get_user():
    while True:
        guess=input('Enter Your Guess(above,below or equal to 7) :-').lower()

        if guess in ['above','below','equal to 7']:
            return guess
        else:
            print('Invalid input.Please enter "above","below",or equal to 7"')  
          

def play_game():

    random_number=random.randint(1,13)
    user=get_user()
    print(f'randomnumber generate :- {random_number}')

    if (user=='above' and random_number>7) or (user=='below' and random_number<7) or (user=='equal to 7' and random_number==7):
        print('You Win')
    else:
        print('Sorry,You Lose.')
print(__name__)
if __name__=='__main__':
    play_game()            


        
      