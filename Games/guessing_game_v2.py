import random

print('... Game Starts ...')
guess_limit = 3
secret_number = random.randint(1, 10)
user_guess = int(input('Make a guess: '))
guess_count = 2
while guess_count <= guess_limit:
    if user_guess < secret_number:
        print('Wrong guess ! Think of a number greater than that.')
        user_guess = int(input('\nTry again: '))
        guess_count += 1
    elif user_guess > secret_number:
        print('Wrong guess ! Think of a number lesser than that.')
        user_guess = int(input('\nTry again: '))
        guess_count += 1
    if user_guess == secret_number:
        print('Well Done ! You guessed it right.')
        print('... Game Ends ...')
        break
else:
    print('Sorry ! No more chances.')
    print('... Game Over ...')
    