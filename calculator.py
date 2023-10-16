#! usr/bin/python3

""" This app offer functionalities
 as a simple calculator

 By  Christian Balinda"""

import sys


logo = r"""
  ---------------------.
 | .-----------------. |
 | | Pythonista Calc.| |   .------------------.  .-------------------.  .-------------------.  .------------------.
 | |_________________| |  | .---------------. | | .----------------. | | .----------------. | | .---------------. |
 |  ___ ___ ___   ___  |  | |     _______   | | | |       __       | | | |    _____       | | | |     _______   | |
 | | 7 | 8 | 9 | | + | |  | |   .` ____  |  | | | |      /  \      | | | |   |_   _|      | | | |   .` ____  |  | |
 | |___|___|___| |___| |  | |  / .`    \_|  | | | |     / /\ \     | | | |     | |        | | | |  / .`    \_|  | |
 | | 4 | 5 | 6 | | - | |  | |  | |          | | | |    / ____ \    | | | |     | |   _    | | | |  | |          | |
 | |___|___|___| |___| |  | |  \ `.___.'\   | | | |  _/ /    \ \_  | | | |    _| |__/ |   | | | |  \ `.___.'\   | |
 | | 1 | 2 | 3 | | x | |  | |   `._____.'   | | | | |____|  |____| | | | |   |________|   | | | |   `._____.'   | |
 | |___|___|___| |___| |  | |               | | | |                | | | |                | | | |               | |
 | | . | 0 | = | | / | |  | '_______________' | | '________________' | | '________________' | | '_______________' | 
 | |___|___|___| |___| |  '___________________' '____________________' '____________________' '___________________'
 |_____________________|
 
"""


def main():
    print(logo)

    new_calc = True
    result = 0
    while True:
        if new_calc:
            try:
                num1 = float(input('What\'s the first number?: '))
            except ValueError:
                num1 = 0
        else:
            num1 = result
        print(' +\n -\n *\n /\n')
        operator = input('Pick an operation: ').strip()
        try:
            next_num = float(input('What\'s the next number?: '))
        except ValueError:
            sys.exit('Incorrect number')

        operations = {'+': add,
                      '-': subtract,
                      '*': multiply,
                      '/': divide}

        if operator:
            function = operations.get(operator)

        calc_continue = input(f'Type \'y\' to continue calculating'
                              f' with {result}, or type \'n\' to'
                              f'start a new calculator: ').lower()

        if calc_continue == 'y':
            new_calc = False
        elif calc_continue == 'n':
            new_calc = True
        else:
            break


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        sys.exit('Can\'t divide a number by zero')


if __name__ == '__main__':
    main()
