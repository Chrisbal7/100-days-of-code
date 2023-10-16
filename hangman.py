#! usr/bin/env python3

""" HANG-MAN :

Guess letters that constitute a random word,
When you guess the right letter, the letter is added
at all the position it can be found in the word, If you
guess wrong you lose a life"""

import random
from libs import *
# from replit import clear


def main():
    word = random.choice(word_list)
    guesses = 6
    guessed_word = list('_' * len(word))

    print(logo)

    # Welcome the user
    print('--- Welcome to the HANG MAN game ---\n' +
          ''.join(guessed_word))

    while guesses:
        letter = input('Guess a letter: ').lower()
        # clear()
        if len(letter) == 1 and letter in word:
            if letter in guessed_word:
                print(f'You are already guessed {letter}')
            else:
                for i in range(len(word)):
                    if word[i] == letter:
                        guessed_word[i] = letter
            if guessed_word == list(word):
                print(''.join(guessed_word))
                print('You win the game!')
                break
        else:
            print(f'You guess {letter}, which it isn\'t in the word. '
                  f'You lose a life!')
            hang_the_man()
            guesses -= 1  # Hang the man

        display_figure()

        if not guesses:
            print('Game over')
            print(f'It was {word}')

        print(''.join(guessed_word))


if __name__ == '__main__':
    main()
