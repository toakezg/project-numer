# module title: Full working script
# version: 0.01
# type: 2
# module order: 2 of 2 (full when with 'name_dob_test')

import traceback

from modules.name_dob_test import name as n, name
from modules.name_dob_test import birthdate as bd

import json
with open('../library/cheiro_dict.json', 'r') as file:
    letter_to_number = json.load(file)
print("\ndictionaries imported")
# imports at the top, print statement not incorrect to go first just recommended to have import at the top

# this is a working module that gets user input, uses that input to do calculations that results in
# single digit numbers #todo double check calcs a right!

def l_p(day, month, year = bd):
    print("\ncalculating LP...")
    # Convert the year, month, and day to strings and concatenate
    print("making strings...")
    date_str = f"{day.zfill(2)}{month.zfill(2)}{year}"

    # Sum all digits in the birthdate
    print("summing...")
    total = sum(int(digit) for digit in date_str)
    print("total reached!\n*dont forget to add the noting of total*")

    # Reduce to a single digit
    print("reducing...")
    while total > 9:
        total = sum(int(digit) for digit in str(total))
    else:
        # Return the final Life Path Number
        print("reduced!\nproviding returning LP")

    return total

def d_n(name = n):
    print('\ncalculating DN')

    # Remove spaces and convert name to uppercase
    print("making strings...")
    name_str = name.replace(" ", "").upper()

    # Convert each letter in the name to a number and sum them
    print("converting..\nsumming...")
    total = sum(letter_to_number.get(letter, 0) for letter in name_str)  # Use .get() to avoid KeyError

    # Reduce to a single digit
    print("summed! \nreducing...")
    while total > 9:
        total = sum(int(digit) for digit in str(total))

    else:
        print("single digit reached! \nreturning DN")
    return total

# Similar approach can be used for calculate_soul_urge_number by filtering only vowels

def s_u(name = n):
    print("\ncalculating SU")
    # Vowels mapping-
    print("mapping vowels in your name")
    vowels_to_number = {'A': 1, 'E': 5, 'I': 9, 'O': 6, 'U': 3}

    # Convert name to uppercase
    print("mapped, converting...")
    name_str = name.upper()

    # Sum numbers corresponding to vowels in the name
    print("summing")
    total = sum(vowels_to_number[letter] for letter in name_str if letter in vowels_to_number)

    # Reduce to a single digit
    print("summed! \n and now reducing")
    while total > 9:
        total = sum(int(digit) for digit in str(total))

    print("single digit found! \n and soon, compounds found will be displayed!")
    print("returning SU")
    return total


try:
    day, month, year = bd.split('-')
    l_p = l_p(day, month, year)
    d_n = d_n(name)
    s_u = s_u(name)
    print("\n \n \nwooohooo! serin-friggin-dippity we got em!\nHere are your Numbers!!!")
    print(f"\nLife Path Number: {l_p}")
    print(f"Destiny Number: {d_n}")
    print(f"Soul Urge Number: {s_u}")

except Exception as e:
    traceback.print_exc()