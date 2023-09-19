#guess number game

from random import *
computer_number = randrange(1,101)
score = 10
while True:
    user_number = int(input('Guess the number 1 to 100'))
    if user_number == computer_number:
        print('You Win with score', score)
        break
    elif user_number < computer_number:
        print('Too Small')
    else:
        print('Too Large')
    score -= 1
