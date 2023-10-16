#! usr/bin/env python3

"""
This program generates a strong password to be used
in websites,
By Christian Balinda
"""

import random
import sys

numbers = '0123456789'
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!@#$%^&*()_+{}:"|<>?~`-=[];\\,./\''


def main():
    try:
        letters_num = int(input('How many letters do'
                                ' you want in the password?\n'))
        numbers_num = int(input('How many numbers do you want ?\n'))
        symbols_num = int(input('How many symbols?\n'))
    except ValueError:
        sys.exit('Invalid input')

    def gen_char_from(num, characters):
        random_chars = ''
        while num:
            random_chars += random.choice(characters)
            num -= 1
        return random_chars

    password = list(gen_char_from(letters_num, letters) +
                    gen_char_from(numbers_num, numbers) +
                    gen_char_from(symbols_num, symbols))

    random.shuffle(password)
    strong_password = ''.join(password)

    print(f'Here is your password: {strong_password}')


if __name__ == '__main__':
    main()
