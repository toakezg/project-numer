
import json
with open('../library/cheiro_dict.json', 'r') as file:
    letter_to_number = json.load(file)
print("dictionaries imported")
# imports at the top, print statement not correct to go first just recommended to have import at top

# this module is dedicated to doing calcs
print("calculating LP...")

def l_p(year, month, day):
    # Convert the year, month, and day to strings and concatenate
    print("making strings...")
    date_str = f"{year}{month}{day}"
    # Sum all digits in the birthdate
    print("summing...")
    total = sum(int(digit) for digit in date_str)
    # Reduce to a single digit
    print("total reached, dont forget to add the noting of total!")
    print("reducing...")
    while total > 9:
        total = sum(int(digit) for digit in str(total))
    # Return the final Life Path Number
    print("reduced.. providing return...")
    return total
print("returned LP")

print('calculating DN')
def d_n(name):
    # Remove spaces and convert name to uppercase
    print("making strings...")
    name_str = name.replace(" ", "").upper()
    # Convert each letter in the name to a number and sum them
    print("converting..summing...")
    total = sum(letter_to_number.get(letter, 0) for letter in name_str)  # Use .get() to avoid KeyError
    # Reduce to a single digit
    print("reducing...")
    while total > 9:
        total = sum(int(digit) for digit in str(total))
    print("single digit reached... returning...")
    return total
print("returned DN")

# Similar approach can be used for calculate_soul_urge_number by filtering only vowels
print("calculating SU")
def s_u(name):
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
    print("single digit found, later compounds too!")
    return total
print("returned SU")


