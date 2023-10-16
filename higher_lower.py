#! usr/bin/python3

""" HIGHER LOWER GAME

The player is asked between two entities which have more,
If he responds right, he gains one point, and he continues the game
until he fails
Then the program print out to the console its score
"""

import random

data = [{ 
    "name": "Instagram",
    "followers_count": 346,
    "description": "Social media platform",
    "country": "United States"},
    {"name": "Cristiano Ronaldo",
     "followers_count": 215,
     "description": "Footballer",
     "country": "Portugal"},
    {"name": "Ariana Grande",
     "followers_count": 183,
     "description": "Musician and Actress",
     "country": "United States"},
    {"name": "Dwayne Johnson",
     "followers_count": 181,
     "description": "Actor and professional wrestler",
     "country": "Portugal"},
    {"name": "Lionel Messi",
     "followers_count": 149,
     "description": "Footballer",
     "country": "Argentina"},
]


def main():
    score = 0
    user_cel = {}
    celebrity1 = get_celebrity()
    # Display their info
    while True:
        celebrity2 = get_celebrity()
        if not celebrity2:
            print(f"Database is empty. Final score = {score}")
            break

        print(f"Compare A: {format_data(celebrity1)}\n vs \n"
              f"Against B: {format_data(celebrity2)}")

        user_input = input("Who has more followers. Type 'A' or 'B': ") \
            .lower().strip()

        if user_input == 'a':
            user_cel = celebrity1
        else:
            user_cel = celebrity2

        celebrity = more_followers(celebrity1, celebrity2)
        if user_cel.get('name', '') == celebrity.get('name', ' '):
            score += 1
            celebrity1 = celebrity
            print(f"You're right. Current score {score}\n")
        else:
            print("Sorry, you're wrong. Final "
                  f"score : {score}")
            break


def get_celebrity():
    if data:
        celebrity = random.choice(data)
        data.remove(celebrity)
        return celebrity


def more_followers(celebrity1, celebrity2):
    followers1 = celebrity1.get('followers_count', 0)
    followers2 = celebrity2.get('followers_count', 0)
    if followers1 > followers2:
        return celebrity1
    return celebrity2


def format_data(account):
    return f"{account.get('name')}, a {account.get('description')}, " \
           f"from {account.get('country')}"


if __name__ == "__main__":
    main()
