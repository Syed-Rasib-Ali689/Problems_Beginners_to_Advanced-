"""
Takes a password as input from the user.
Checks the following conditions:

Length is at least 8 characters
Contains at least one uppercase letter
Contains at least one lowercase letter
Contains at least one digit
Contains at least one special character (e.g., !@#$%^&*)

Prints which conditions are met and which are not.
Prints an overall result: Strong (all conditions met), Medium (3-4 conditions met), or Weak (2 or fewer conditions met).
"""

import string

password = input("Enter your password: ")

has_uppercase = any(char.isupper() for char in password)
has_digit = any(char.isdigit() for char in password)
has_lowercase = any(char.islower() for char in password)
has_special = any(char in string.punctuation for char in password)
length_ok = len(password) >= 8

if has_uppercase:
    print("The password contains at least one uppercase letter.")
else:
    print("The password does not contain any uppercase letters.")

if has_digit:
    print("The password contains digits.")
else:
    print("The password does not contain any digits.")

if has_lowercase:
    print("The password contains lowercase letters.")
else:
    print("The password does not contain any lowercase letters.")

if has_special:
    print("Password contains special characters.")
else:
    print("Password does not contain special characters.")

if length_ok:
    print("Password has at least 8 characters.")
else:
    print("Password does not have at least 8 characters.")

score = sum([length_ok, has_uppercase, has_lowercase, has_digit, has_special])

if score == 5:
    print("Overall Result: Strong")
elif score >= 3:
    print("Overall Result: Medium")
else:
    print("Overall Result: Weak")