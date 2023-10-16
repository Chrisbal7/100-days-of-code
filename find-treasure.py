#! /usr/bin/env python3

"""

This program is a game that asks the user to find out
a treasure by guessing!

By Christian Balinda

"""


def main():
    print('Welcome to the Treasure Island, \n'
          ' Your mission is to find the treasure')

    direction = input('You\'re at cross road. '
                      'Where do you want to go? type "left" or "right" : ')

    if direction.lower() == 'left':
        action = input('You came to a lake. there is an island in the '
                       'middle of the lake. '
                       'Type "wait" to wait a boat. '
                       'Type "swim" to swim across.')
        if action.lower() == 'wait':
            colour = input('You arrive ath the island unharmed. '
                           'There is a house with thr]]]ee doors. '
                           'There is a house with thr]]]ee doors. '
                           'One red, one yellow and one blue. '
                           'Which colour do you choose? ').lower()

            if colour == 'yellow':
                print('You find the treasure. You won')
                return True
            elif colour == 'red':
                print('You enter in a room full of fire.', end=' ')
            else:
                print('You\'ve entered the room of beasts')

    else:
        print('You fall in the hole.', end=' ')

    print('Game over!')
    return False


if __name__ == '__main__':
    main()
