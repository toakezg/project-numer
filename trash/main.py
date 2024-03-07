import traceback

# todo = redo this module
# todo = integrate three modules: 'dobbys_intro_v001.py', 'get_ui_v0.1.py', 'lds_n_calcs_v0.1.py"
# todo = import and compile tracebacks (include what module they are referring to)
# todo = adjust logic and structure where needed
# todo = check name references, module references, function calls
# todo = remember print statements for indicators
# todo + tracebacks again
# todo = reword, restructure
# todo = +++ play play play +++
# todo = test , debug , test , debug , test , debug
# todo = add any relevant todos as you go along


# those three modules will make the total of main script of atleast the section of the project that covers
# getting LP, DN, SU numbers.
#

from name_dob import name, birthdate

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
    year, month, day = birthdate.split('-')

    # Calculate the Life Path Number using the extracted date parts
    life_path_number = nc.l_p(year, month, day)
    print(f"Life Path Number: {life_path_number}")
except Exception as e:
    traceback.print_exc()
