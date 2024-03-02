# Task: Use 'while loop' to verify user input of age
#
# 1. Loop until age is all digits
# Look at this code:
#
# Ask user for their age
# age = input("What is your age? ")
#
# print(f" Your age is {age}")
# The problem with this code is that even if the user is 20, they could enter "20" or "twenty". Let's standardise the input to get the age as digits...
#
# Starting code - replace comments in CAPITALS with your code:
#
# SET VARIABLE user_prompt TO TRUE
user_prompt = True
# PUT BEGINNING OF WHILE LOOP HERE - SHOULD LOOP WHILE user_prompt IS TRUE
while user_prompt:
    age = input("What is your age? ")
    if age.isdigit() and 0 < int(age) <= 117:
        user_prompt = False
    else:
        print("Please enter your age as a valid number")

print(f"Your age is {age}")
# Hints:
#
# To check is 'age' is all digits, use the 'age' string's method .isdigit()
#
# 2. Also check age is in the correct range
# Our code now works to stop our user from inputting strings, floats, and negative numbers, but at the moment the user could say they are 356000 years old if they want.
#
# Assuming the oldest person alive today is 117, modify your code to only allow a maximum of 117 as the age.
#
# Hint:
#
# You already have an 'if statement' to check 'age' is all digits. Use the 'and' keyword to ALSO check 'age' is not too high.