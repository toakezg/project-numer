import traceback

print("""
 \nHeya, 
 .*.<[O.O]>,,  
 My i am Dobby 
 My job is to guide you through the magical process
 of getting your hands onto your very own tailored
 Destiny, Soul Urge, and Life Path numbers!!
 \n
 .<[O.O]>.
 On this very exciting journey of exploration,
 discovery, and great meaning, I will happily assist in
 keeping you on path. As this may be your first time interacting 
 with one of the magical systems of numbers, I'll provide a
 great place to start, keeping things simple and hassle-free!  
 \n
 ...<[O.O]>...
 When you are ready to explore what numbers are hidden 
 within your name and birthdate, and soon, what this may entail,
 follow my one small step at a time, I'm here for you!""")

def get_user_input():


    while True:
        name = input("\nPlease enter your name (or press Enter to skip): ")
        if not name:
            print("Name was not provided.")
        else:
            print(f"Name entered: {name}")

        year = input("Please enter the year of your birth (YYYY): ")
        while not year.isdigit() or len(year) != 4:
            print("Invalid input. Please enter the year as four digits (e.g., 1994).")
            year = input("Year (YYYY): ")
        print(f"Year entered: {year}")

        month = input("Please enter the month of your birth (1-12): ")
        while not month.isdigit() or not 1 <= int(month) <= 12:
            print("Invalid input. Please enter the month as a number between 1 and 12.")
            month = input("Month (1-12): ")
        print(f"Month entered: {month}")

        day = input("Please enter the day of your birth (1-31): ")
        while not day.isdigit() or not 1 <= int(day) <= 31:
            print("Invalid input. Please enter the day as a number between 1 and 31.")
            day = input("Day (1-31): ")
        print(f"Day entered: {day}")

        print("\nPlease confirm the following details:")
        print(f"Name: {name if name else 'Not provided'}")
        print(f"Birthdate: {year}-{month.zfill(2)}-{day.zfill(2)}")
        confirmation = input("Is this information correct? (yes/no): ").lower()
        if confirmation == 'yes':
            break
        else:
            print("Let's try again...\n")

    return name, f"{year}-{month.zfill(2)}-{day.zfill(2)}"

try:
    print("hello world")
    name, birthdate = get_user_input()
    print(f"Collected data: Name = {name}, Birthdate = {birthdate}")
except Exception as e:
    traceback.print_exc()


