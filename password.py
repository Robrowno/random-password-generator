# random password generator
import os
import sys
import random
import string

password_length = 18

possible_chars = [string.ascii_letters, string.digits, "!£$%&*@?"]

chars = []

# iterate through possible_chars and append in to chars list
for list in possible_chars:
    for item in list:
        chars.append(item)

def generate_password():
    """
    Generates a random password from
    using chars above
    """
    password = []
    # picks a random character and appends into the password list
    for i in range(password_length):
        random_char = random.choice(chars)
        password.append(random_char)
    # returns a string of the new password
    return "".join(password)

print(generate_password)
print("Hello World")