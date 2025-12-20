import random
secret_num = random.randint(1, 50)
print('im thinking of a number, can you guess it?')
guess = int(input('your guess: '))
if guess < secret_num:
    print('too low!')
elif guess > secret_num:
    print('too high!')
elif guess == secret_num:
    print('you guessed it!')
else:
    print('error')



