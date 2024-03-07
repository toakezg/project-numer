
# module title: 00(c) - call list
# version: 00.01
# type: 1
# module order: 0 of 0


# a collection of print calls of functions and to get their return values
# not a 'working/running module' due to no imports being listed
# maybe provide relevant imports along with calls
#todo if deemed fit too, provide imports and configure calcs to return 0 if no input is provided

print(f"Name entered: {name}")

print(f"Year entered: {year}")
print(f"Month entered: {month}")
print(f"Day entered: {day}")
print(f"Birthdate: {day.zfill(2)}-{month.zfill(2)}-{year}")

name, birthdate = get_user_input()
print(f"Collected data: Name = {name}, Birthdate = {birthdate}")

print(f"\nLife Path Number: {l_p}")
print(f"Destiny Number: {d_n}")
print(f"Soul Urge Number: {s_u}")