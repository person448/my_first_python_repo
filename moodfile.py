user = input('what is your name?: ')
mood = input('how are you feeling today? sad, mad, happy, or bored?: ')
if mood == 'sad':
    print(f'cheer up {user} it will always get better!')
elif mood == 'mad':
    print(f'its okay {user} just take 5 deep breaths and read a book!')
elif mood == 'happy':
    print(f'keep smiling {user} you are doing great!')
elif mood == 'bored':
    print(f'try learning something new {user} like coding or a new language!')
else:
    print('dont understand. try saying you mood in lowercase or put a valid mood from the choices given.')
