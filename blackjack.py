#! usr/bin/python3

""" BLACKJACK GAME
The player wins the game if the sum of cards picked up
doesn't exceed 21 and if it is greater than the sum of the opponent
The player gets two cards, and then had a choice to select
another card,
If the player exceed 21, he loses the game
"""

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def main():
    while True:
        play_blackjack = input('Do you want to play a game of BlackJack? '
                               'Type \'y\' or \'n\': ').lower().strip()
        if play_blackjack == 'y':
            my_cards = get_card(2)
            computer_cards = get_card()

            print(f'Your cards: {my_cards}\n'
                  f'Computer\'s cards: {computer_cards}')

            pick_card = input('Type \'y\' to get another card, '
                              'type \'n\' to pass').lower().strip()
            if pick_card == 'y':
                picked_card = get_card()
                my_cards += picked_card
                print(f'You picked up a {picked_card}')

            computer_cards += get_card()

            you = {'player': 'you', 'cards': my_cards}
            computer = {'player': 'computer', 'cards': computer_cards}
            winner = judge(you, computer)

            print(f'Your final hand: {my_cards} \n'
                  f'Computer\'s final hand: {computer_cards}\n'
                  f"{winner.get('player', 'Nobody')} win")
        else:
            break


def get_card(number_of_cards=1):
    card_list = []
    for num in range(number_of_cards):
        card_list.append(random.choice(cards))
    return card_list


def judge(player1, player2):
    score1 = sum(player1.get('cards', []))
    score2 = sum(player2.get('cards', []))

    if score1 <= 21:
        if score1 > score2:
            return player1
        elif score1 == score2:
            return dict()
    else:
        if 11 in player1.get('cards', []):
            if score1 - 10 > score2:
                return player1
            elif score1 - 10 == score2:
                print('Draw')
                return dict()
    return player2


if __name__ == '__main__':
    main()
