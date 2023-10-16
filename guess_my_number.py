#! usr/bin/python3

""" GUESS MY NUMBER GAME
The computer generates a mystery number, then the user have
attempts to guess the number, the program gives hints if the guessed number
is too high or too low,
The game is lost when the user runs out of numbers of attempts,
The player wins the game when he guessed right

Christian Balinda
"""

import random


def main():
    mystery_number = random.randint(1, 100)
    print('Welcome to the Number Guessing Game')
    print('I\'m thinking of a number between 1 and 100')
    attempts = 0
    difficulty = input('Choose a difficulty. '
                       'Type \'hard\' or \'easy\'').lower().strip()

    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5

    while attempts:
        # Guess the mystery number
        print(f'You have {attempts} attempts remaining to guess the number')
        try:
            guessed_num = int(input('Guess a number: ').strip())
        except ValueError:
            print('Incorrect number, you lose one attempt')
            attempts -= 1
            continue

        if guessed_num > mystery_number:
            print('To high')
        elif guessed_num < mystery_number:
            print('Too low')
        else:
            print(f'The mystery number is {guessed_num}\n'
                  f'You win')
            break

        if attempts > 1:
            print('Guess again')
        else:
            print('Game Over')
        attempts -= 1


if __name__ == '__main__':
    main()
