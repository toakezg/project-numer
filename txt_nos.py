import shutil
import json

def print_line(character='-'):
    # Get the size of the terminal
    terminal_width = shutil.get_terminal_size().columns

    # Print the character across the terminal width
    print(character * terminal_width)


# Usage
print_line()  # This will print a line of '-' characters
print('\n*Welcome to another start of Numbers:*')
print("\nloading dictionaries...")

# Load Cheiro's Numerology Dictionary from JSON
with open('cheiro_dict.json', 'r') as file:
    cheiro_dict = json.load(file)

print("dictionaries loaded successfully")
# Continue with the rest of your main script here...
print("setting up translation functions...")


def text_to_numerology(text):
    numerology_values = []
    for char in text.upper():
        if char in cheiro_dict:
            numerology_values.append(str(cheiro_dict[char]))
        else:
            numerology_values.append(' ')  # Non-alphabetic characters are kept as space or handled differently
    return ' '.join(numerology_values)

print("translation functions done son")
print("\nloading UI...")

while True:

    print("\nnumerology systems")
    print("version 0.001 as of 24-02-24")
    print("currently letter to number translation")
    # to be expanded on, more deeply in time
    # learning the use of implementing Git for version control would be handy
    choice = input("\nEnter text to convert to numerological values (or 'exit' to quit): ")
    if choice.lower() == 'exit':
        break

    print("\nNumerological Value:", text_to_numerology(choice)) # should be wrapped

    print_line()
