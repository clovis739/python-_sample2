from string import ascii_letters, digits, punctuation
from itertools import product

number = '@clovertt'
for passcode in product(ascii_letters + digits + punctuation, repeat = 4):
    if passcode == number:
        print('seen ')
    else:
        print('not seen')
    print(passcode)
