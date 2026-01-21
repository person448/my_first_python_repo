def decode_ceaser_cipher(text, shift):
    brackets = []
    for hi in text:
        numbers = ord(hi)
        new_numbers = chr(numbers - shift)
        brackets.append(new_numbers)
    print(brackets)
user = input('enter text you want to decode:')
decode_ceaser_cipher(user, 3)