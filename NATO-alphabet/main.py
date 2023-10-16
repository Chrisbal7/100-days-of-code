"""
This program encodes any input string into a list
based on the NATO alphabet
"""

import csv


def extract_data():
    with open("nato_phonetic_alphabet.csv") as nato_alphabet_file:
        reader = csv.reader(nato_alphabet_file)
        return {alphabet: nato_alphabet for alphabet, nato_alphabet in reader
                if reader.line_num != 1}


def main():
    data = extract_data()
    input_str = input("Enter a name: ").upper()
    nato = [data[letter] for letter in input_str if letter in data.keys()]
    print(nato)


if __name__ == "__main__":
    main()
