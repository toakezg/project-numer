import traceback

# module title: Dobbys calculations
# version: 0.01
# type: #1 to be 2
# module order: 3 of ...

# module 3 - calculations

from modules.name_dob_test import name as n, name
from modules.name_dob_test import birthdate as bd

import json
with open('../library/cheiro_dict.json', 'r') as file:
    letter_to_number = json.load(file)

print("\ndictionaries imported")
print("other imports imported")
print("\nloading calculations workspace")
print("loading methods:\n   version:0.01 type: 1 (atm)")
# imports at the top, print statement not incorrect to go first just recommended to have import at top
# at a later point into integration of this module to a main script, the imports maybe will have to be
# moved with any variables relating to names, and calls being faced and changed correctly if a need arises

# this module is dedicated to doing calcs
# this module is structured to have 3 'def' functions being the 3 calculation methods used to get
# the desired result
# im not sure if this can later act as a dictionary of methods where different calculations in here
# can be called on with another part of the project, for other desired results
# id think it will

# in this def function below, within the brackets, im not sure if = bd is needed, but was there when it started
# working. and may be subject to change when integrated into a main script
# my logic being that name_dob was called from the input 'birthdate' which would can referred to as bd
# and here where it required me to input in brackets those statements or calls, i also summed that
# all three can be referred to as bd and later used how i previously seen the main script nc."  " , and so on
# will all be worked out #sus #todo holy crapoli todo highlights, noice!!!.'

def l_p(day, month, year = bd):
    # 'shadows in name:...' indicated in a yellow error, yet seems to be a sign of success atm
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

# while revising above, I found it seems pretty self-explanatory now, thank the lord!
# i think the issues i was facing was the string being separated, functions not being called
# indentation issues, and other minor tweaks had to be made
# was so happy when the next few print functions were executed and provided the correct, #todo double check results
#

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

# all these tracebacks to be input to main hopefully still successfully aids in the process and
# identifying errors without be to widely used by not yet providing which module their related to
# #todo might have to provide which module the traceback try(s) are within.

# #todo celebrate!!!!


