#! usr/bin/python3

""" This program simulates a bid in real life
When there is no one to bid, the buyer with the
highest price won the auction

By Christian Balinda
"""


def main():
    print('Welcome to the Bid-Auction ')
    winner_bid = {}
    bids = []
    # Bid until there is no bidder,
    while True:
        name = input('Enter the name: ')
        try:
            auction = int(input('How much are you going to bid: $'))
        except ValueError:
            auction = 0
        bids.append({'name': name, 'amount': auction})
        if input('Is there any others bid? type \'yes\''
                 ' or \'no\'').lower() == 'no':
            break

    for bid in bids:
        if bid['amount'] > winner_bid.get('amount', 0):
            winner_bid['name'] = bid['name']
            winner_bid['amount'] = bid['amount']

    print(f"{winner_bid.get('name', 'Nobody')} wins the auction "
          f"with ${winner_bid.get('amount', 0)}")


if __name__ == '__main__':
    main()
