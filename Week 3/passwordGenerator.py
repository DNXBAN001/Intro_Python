# Name : Bandile Danxa
# Date : 18 May 2020
# Submission 4 - PasswordGenerator
#This program generates a random password that should satisfy some specific criteria
#Password must have atleast 1 lower-case character, 1 upper-case character, 1 special-case character
#Password must have atleast 1 lower-case character and have a minimum of 8 characters

import random

def passwordGenerator():
    lowerCaseChars = ['m', 'n', 'a', 'o', 'd', 'j', 'g']
    upperCaseChars = ['Q', 'X', 'Z', 'D', 'E', 'M', 'G']
    specialCaseChars = ['@', '#', '*', '_', '-', '+', '!']
    numberChars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    password = random.choice(upperCaseChars)+random.choice(lowerCaseChars)+random.choice(numberChars)+random.choice(specialCaseChars)
    password += password

    return password


print("The generated password is : "+ passwordGenerator())

