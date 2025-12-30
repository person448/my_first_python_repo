import random
secret_num = random.randint(1, 10)
attempts = 0
while True:
    guess = int(input('guess a number between 1 and 10:'))
    attempts += 1

    if guess < secret_num:
        print('too low')
    elif guess > secret_num:
        print('too high')
    elif guess == secret_num:
        print(f'you guessed it! the number was {secret_num}. it took you {attempts} attempts to guess the number.')
    else:
        print('error')
