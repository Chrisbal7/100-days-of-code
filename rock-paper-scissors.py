#!usr/bin/env python3

"""

This program is about a game called rock-paper-scissors
That program is going to be played by the user VS the computer,
The rock lose over the paper,
The paper lose over the scissors,
The scissors lose over the rock

"""

import random, sys


def main():
    players = {}
    choices = {0: 'rock',
               1: 'paper',
               2: 'scissors',
               }
    # User turn
    try:
        choice1 = int(input('What do you chose? '
                            'Type 0 for Rock, '
                            '1 for Paper, '
                            '2 for Scissors, '))
        players.setdefault(choice1, 'You')
        if choice1 > 2:
            sys.exit('Unknown choice!')
    except ValueError:
        sys.exit('Invalid input')
    # Computer turn
    choice2 = random.choice([0, 1, 2])
    players.setdefault(choice2, 'The computer')

    # Display choice
    print(f'You choose {choices[choice1].upper()}\n'
          f'The computer choose {choices[choice2].upper()}\n')
    winner = None
    if abs(choice1 - choice2) == 1:
        winner = players.get(max([choice1, choice2]), None)
    elif choice1 - choice2 == 0:
        print('It\'s a draw')
        return None
    else:
        winner = players.get(min([choice1, choice2]), None)

    print(f'{winner} win the game')
    return winner


if __name__ == '__main__':
    main()
