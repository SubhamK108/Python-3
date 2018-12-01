import os
os.system('clear')
import random
import sys
print('I am Guessing a number between 0 and 10...')
ai = random.randint(0, 10)
c = 1
user = int(input('Make a Guess : '))
while True:
    if user == ai:
        print(f'You are Correct !\nNumber of Attempts : {c}\nWell Done...')
        sys.exit()
    elif user < ai:
        print(f'Think of a number greater than {user}')
        user = int(input('Try Again : '))
        c = c + 1
    else:
        print(f'Think of a number lesser than {user}')
        user = int(input('Try Again : '))
        c = c + 1
input('Press any Key to Exit...')
