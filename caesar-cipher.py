#! usr/bin/python3

"""
 ----------Caesar Cipher---------
This program is using Caesar Cipher to encrypt messages
So only the person who knows the shift number can be able
to decode

By Christian Balinda
"""
import sys
from libs import caesar, cipher

letters = 'abcdefghijklmnopqrstuvwxyz' \
          'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
          ' ~!@#$%^&*()_+{}:"|<>?[];\'\\,./\n'

print(caesar, cipher)


def main():
    end = False
    while not end:
        while True:
            desired_action = input('Type \'encode\' to encrypt, '
                                   'type \'decode\' to decrypt \n')
            if 'code' in desired_action:
                break

        message = input('Type your message: \n').strip()
        try:
            shift_number = int(input('Type the shift number: \n'))
        except ValueError:
            sys.exit('Incorrect input')

        if desired_action == 'encode':
            print(f'Here is your encoded result: '
                  f'{encode(message, shift_number)}')

        elif desired_action == 'decode':
            print(f'Here is your decoded result: '
                  f'{decode(message, shift_number)}')

        if input(f'Type \'yes\' if you wanna go again. '
                 f'Otherwise type \'no\' :').lower() == 'no':
            print('End of the encryption/decryption')
            end = True


def encode(message, shift_num=1):
    encrypted_msg = ''
    for letter in message:
        encrypted_index = letters.index(letter) + shift_num
        while encrypted_index > len(letters) - 1:
            encrypted_index -= len(letters) - 1
        encrypted_msg += letters[encrypted_index]

    return encrypted_msg


def decode(message, shift_num=1):
    decrypted_msg = ''
    for letter in message:
        decrypted_index = letters.index(letter) - shift_num
        while decrypted_index < 0:
            decrypted_index += len(letters) - 1
        decrypted_msg += letters[decrypted_index]

    return decrypted_msg


if __name__ == '__main__':
    main()
