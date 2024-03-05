import traceback

# module title: Dobbys questions
# version: 0.01
# type: 2
# module order: 2 of ...

#  module 2 - get user input

# when integrated with the main script, all tracebacks maybe listed at bottem, with one import traceback (at top)
# this would be to create a script that only has one import of a trace back, that works throughout the modules
# hopefully... makes sense though!

# ive found it helps to separate blocks into sections via  a line between different actions
# it helped clear up and see what it is doing, and to enable working with it to become easier

# keep up with labelling versions and intros to modules as a way to see them being executed in the main script
print("\nnow using user input module version:0.001 type:2 (customized)")
# apart from providing a clear indication which module is in use, starting now this is version: ""
# and also I have labeled the 'type' of user input module, being type 2.
# where a type 1 module will be a generic script
# a type 2 module will be a customized scripts
# as this script will be customized to continue in the manner of how dobbys guiding the user
# to create a more user-friendly environment

print("\nstarting to prepare dobbys questions..")
# this print is to indicate that the module is now in use being executed from the main script
# this will help indentify any flow errors in the process or the way it executes the main module

def get_user_input():
    # script in this block goes towards getting a 'value' of the function
    # with the return at the bottem
    # the return at the bottem returns that value of what the function will output when called on
    # seen further in the script
    while True:
        # while True starts the loop to this block which breaks upon the successful confirmation
        # by the user that what they entered is the correct details that will be used in the next module
        name = input("\nPlease enter your name full name here (or press Enter to skip): ")
        # a general input prompt, the space after ':" before the last '"' i think is necessary
        # but idea of thats where i enter different answers i think I am wrong in thinking that
        # it would be a bit more complex but i believe thats where a list might be made for example
        # and well actually im not sure how a more multi variable question/reply
        # input section would be worded to provide an example of where my thoughts are
        # I just think it might be involved round the 'if' 'else' areas with a list or other form
        # of correspondence
        if not name:
            print("Name was not provided.")
            # 'if' a loop function? when with else? this function here starts a type of loop
            # where if the name was not provided, oh no, I'm incorrect, I don't think it loops back to
            # prompting a name, 'if' isn't a loop its #sus
        else:
            print(f"Name entered: {name}")
            # 'else' is provided to take 'if's place if the name is indeed entered.

        # another simple input prompt though with a bit more to it, seems to be the goto project to learn this
        year = input("\nPlease enter the year of your birth (YYYY): ")
        while not year.isdigit() or len(year) != 4:
            print("Invalid input. Please enter the year as four digits (e.g., 1994).")
            # the 'while note' is pretty self-explanatory, id need to note the 'year.isdigit()' or 'len(year) !+ 4:
            # im not sure what 'len' is, but relates to year being a number of 4 digits. and maybe the
            # year is, part is to define the year has to be in the format of digits, or it will trigger the invalid
            year = input("Year (YYYY): ")
        print(f"Year entered: {year}")

        month = input("\nPlease enter the month of your birth (1-12): ")
        while not month.isdigit() or not 1 <= int(month) <= 12:
            # while not a digit = invalid input, and/or not less 1 or more than 12 = invalid input
            print("Invalid input. Please enter the month as a number between 1 and 12.")
            month = input("Month (1-12): ")
        print(f"Month entered: {month}")
        # each input has a print at the bottem to indicate and in a way confirm the input proves to be valid

        day = input("\nPlease enter the day of your birth (1-31): ")
        while not day.isdigit() or not 1 <= int(day) <= 31:
            print("Invalid input. Please enter the day as a number between 1 and 31.")
            day = input("Day (1-31): ")
        print(f"Day entered: {day}")

        print("\nPlease confirm the following details:")
        print(f"Name: {name if name else 'Not provided'}")
        # next it an example of taking values and making them part of a string
        # the 'f'' part states it is a 'f-string' which i cant remember its exact definition,
        # but one of its base concepts can be understood, by being a string
        # have to input definition of "f" string"
        print(f"Birthdate: {day.zfill(2)}-{month.zfill(2)}-{year}")
        # this next part is a clear example of a way to confirm what the information
        # that the input has gathered so far (if the user input is correct)
        # with a simple loop, is it a loop or condition(al)?
        confirmation = input("Is this information correct? (yes/no): ").lower()
        if confirmation == 'yes':
            break
        else:
            print("Let's try again...\n")

    return name, f"{day.zfill(2)}-{month.zfill(2)}-{year}"
    # as stated near the start of the script module,
    # the return value is the value
    # the function will provide when called

# up next is the bottom side of a traceback function structured as a block
# from what ive gathered, within 'try:' you list possible lines or functions ect. that may be having issues
# and will provide more information or atleast help indicate the areas with issues present
# and help getting the script ready to go
# as mentioned earlier, the main script will have to compile these traceback 'try(s)'  under one import
# and try for a successful approach that way.
# as you amend the script with the correct or more suitable methods lines in the within 'try' can be removed
# and rechecked for reassurance of being fixed and/or workable
try:
    name, birthdate = get_user_input()
    print(f"Collected data: Name = {name}, Birthdate = {birthdate}")
except Exception as e:
    traceback.print_exc()