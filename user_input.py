# this is to act as a user input module (dedicated)
print("obtaining user input")
def get_user_input():
    name = input("Please enter your full name: ")
    year = input("Enter your birth year (YYYY): ")
    month = input("Enter your birth month (MM): ")
    day = input("Enter your birth day (DD): ")
    print("user input collected, is this it? later include loop for options yes no")
    return name, year, month, day
# make sure return function works
# later include while True loop, if or else, break. and a prompt to ask if it is the correct return
# implement into main script, can be made more simple! or have a simple and one for different situations.