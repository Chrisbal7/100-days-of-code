#!usr/bin/env python3

""" 
    This program calculate the total bill
    you should pay based on the price of the meal, 
    the numbers of people who split the bill, and the tip
    
    Made by Christian Balinda
"""

import sys


def main():
    print('Welcome to the tip calculator')

    try:
        bill = float(input('What was the total bill? $').strip())
        if not bill:
            sys.exit('Each person should pay $0')

        people_num = int(input('How many people have '
                               'to split the bill? ').strip())
        perc = float(input('What percentage of the tip'
                           'would you like to give? 10, 12 or 15? : ').strip())
    except ValueError:
        sys.exit('Incorrect input')

    if people_num:
        personal_bill = bill / people_num
        tip = personal_bill * (perc / 100)
        total = round(personal_bill + tip, 1)
        print(f'Each person should pay :${total}')
        return total
    else:
        print('The number of people can\'t be 0')


if __name__ == '__main__':
    main()
