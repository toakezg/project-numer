import traceback

from name_dob import get_user_input

import numer_calcs as nc

print("imports done")

name, year, month, day = get_user_input()
life_path = nc.l_p(year, month, day)
destiny_number = nc.d_n(name)
soul_urge = nc.s_u(name)

print("passed the crap i dunno and.. totals should be next")
print(f"Life Path Number: {life_path}")
print(f"Destiny Number: {destiny_number}")
print(f"Soul Urge Number: {soul_urge}")
print("done done done done done done done odne odne ndone done done done done done done done!!!!!!")

try:
    name, birthdate = get_user_input()
    print(f"Collected data: Name = {name}, Birthdate = {birthdate}")

    # Extract year, month, day from the birthdate string
    day, month, year = birthdate.split('-')

    # Calculate the Life Path Number using the extracted date parts
    life_path_number = nc.l_p(day, month, year)
    print(f"Life Path Number: {life_path_number}")
except Exception as e:
    traceback.print_exc()