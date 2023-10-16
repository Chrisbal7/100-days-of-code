#!usr/bin/env python3

""" This program suggests a band name for anyone who 
may want to get inspired 

made by Christian Balinda"""


def main():
    # Get information from the user
    print('Welcome to the Band Name Generator')
    city_name = input('In which city you grew up in?: \n')
    pet_name = input('What\'s your pet\'s name?: \n')
    
    # Suggests a name based on information provided
    print(f'Your band name could be {city_name} {pet_name}')
    

if __name__ == '__main__':
    main()
    