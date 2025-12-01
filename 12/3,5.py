import re

# read username and password from keyboard
username = input("Podaj swój login: ")
password = input("Podaj swoje hasło: ")

# pattern (criteria) for username and password
username_pattern = r'^[a-z0-9]{6,}$'
password_pattern = r'^[a-zA-Z0-9_]{8,}$'

# check if username and password are ok
username_match = re.match(username_pattern,username)
password__match = re.match(password_pattern,password)

# print results
if username_match and password__match:
   print("Poprawne dane")
else:
   print("Podane dane nie są poprawne")