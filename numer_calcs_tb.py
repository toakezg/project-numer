import traceback

from name_dob_test import name as n, name
from name_dob_test import birthdate as bd

import json
with open('cheiro_dict.json', 'r') as file:
    letter_to_number = json.load(file)
print("\ndictionaries imported")
# imports at the top, print statement not incorrect to go first just recommended to have import at top

# this module is dedicated to doing calcs

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
        print("reduced!\nproviding return...")

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
    print("reducing...")
    while total > 9:
        total = sum(int(digit) for digit in str(total))

    else:
        print("single digit reached! \nreturning...")
    return total

# Similar approach can be used for calculate_soul_urge_number by filtering only vowels

def s_u(name = n):
    print("\ncalculating SU")
    # Vowels mapping-
    print("mapping...")
    vowels_to_number = {'A': 1, 'E': 5, 'I': 9, 'O': 6, 'U': 3}

    # Convert name to uppercase
    print("converting...")
    name_str = name.upper()

    # Sum numbers corresponding to vowels in the name
    print("summing")
    total = sum(vowels_to_number[letter] for letter in name_str if letter in vowels_to_number)

    # Reduce to a single digit
    print("reducing")
    while total > 9:
        total = sum(int(digit) for digit in str(total))

    print("single digit found,\n and soon, compounds found will be displayed!")
    print("returning SU")
    return total


try:
    day, month, year = bd.split('-')
    l_p = l_p(day, month, year)
    d_n = d_n(name)
    s_u = s_u(name)
    print(f"\n \n \nLife Path Number: {l_p}")
    print(f"Destiny Number: {d_n}")
    print(f"Soul Urge Number: {s_u}")
except Exception as e:
    traceback.print_exc()