print("Task 1 - Task: Concatenate these variables with different data types" )
x = 2
y = 5.4
z = " there's now a number 25.4 unless we put a space in!"

print(str(x) + str(y) + z)

# -------------------------------------------------------------------------------------------------------------------------------------------------
print("\nTask 2 - Task: Convert this string to an int and float" )
int_string = "6"

# convert int_string to an integer
int_int = int(int_string)
# after converting, print its data type to the screen
print(type(int_int))

# convert int_string to float
int_float = float(int_string)
# after converting, print its data type to the screen

print(type(int_float))

# -------------------------------------------------------------------------------------------------------------------------------------------------
print("\nTask 3 - Task: Print line as an f-string" )
name = "Lassie"
years = 7
height_cm = 60.2

# print these variables in an f-string so that it outputs this to the screen:
# "Lassie is 7 years old and 60.2 cm tall."
print(f"{name} is {years} years old and {height_cm} cm tall.")

# -------------------------------------------------------------------------------------------------------------------------------------------------
print("\nTask 4 - Task: Use f-strings to format numbers" )
pi = 3.14159265359

# Use an f-string to print pi to 3 decimal places e.g. 'Pi to 3 decimal places: <value>'
print(f"Pi to 3 decimal places: {pi:.3f}")
#print("Pi to 3 decimal places: {}".format(round(pi,3)))
# Use an f-string to print pi to 5 decimal places e.g. 'Pi to 5 decimal places: <value>'
print(f"Pi to 3 decimal places: {pi:.5f}")


score = 16
max_score = 26
score_as_decimal = score/max_score

# Use an f-string to print 'score_as_decimal' e.g. 'You scored 0.6153846153846154' (no % sign)
print(f"You scored {score_as_decimal}")
# Use an f-string to print 'score_as_decimal' formatted as a percentage e.g. 'You scored 61.538462%'
print(f"You scored {score_as_decimal:%}")
# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to 2 decimal places e.g. 'You scored 61.54%'
print(f"You scored {score_as_decimal:.2%}")
# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to a whole number e.g. 'You scored 62%'
print(f"You scored {score_as_decimal:.0%}")

# -------------------------------------------------------------------------------------------------------------------------------------------------
print("\nTask 5 - Task: Boolean methods for strings" )

hi = "Hello World!"

# find out if 'hi' is made up of letters only (use one of the strings methods) - print the boolean to the screen
print(hi.isalpha())
# find out if 'hi' is made up only of lowercase letters (use one of the strings methods) - print the boolean to the screen
print(hi.islower())
# find out if 'hi' is made up only of uppercase letters (use one of the strings methods) - print the boolean to the screen
print(hi.isupper())
# find out if 'hi' ends with an exclamation mark (use one of the strings methods) - print the boolean to the screen
print(hi.endswith("!"))
# find out if 'hi' starts with a capital "h" (use one of the strings methods) - print the boolean to the screen
print(hi.startswith("H"))

# -------------------------------------------------------------------------------------------------------------------------------------------------
print("\nTask 6 - Task: Understanding 'None' in Python" )
# What is None in Python?
# When is it commonly used?
# What's the equivalent in some other programming languages?
# In Python, None is a special constant representing the absence of a value or a null value. It is a singleton object of the NoneType.
#
# It's commonly used as a placeholder or default value, especially when you want to signify that a variable or a function does not return any meaningful result or when a value has not been initialized yet.
#
# In other programming languages, the equivalent of None in Python can vary:
#
# In JavaScript, null is used for similar purposes.
# In Java, C#, and other statically typed languages, null serves the same role.
# In some languages like C++, nullptr is used to denote a null pointer.
# When you convert None to a boolean in Python, it evaluates to False.
# Most important: What happens when you convert None to a boolean?
print(bool(None)) # Output is false
# Write a piece of Python code to prove it
# Write a piece of Python code to...
# assign x to be None
x = None
# print whether my variable x is equal to None
# print(x == None)
print(x is None)

# -------------------------------------------------------------------------------------------------------------------------------------------------
print("\nTask 7 - Task: Calculate Year of Birth")
# First part
# define the variables age_int and name_str (set dummy/default/initial values)
age_int = 23
name_str = "Ramon"
current_year = 2024
# make a calculation for the year in which the person was born
year_of_birth = current_year - age_int
# print out "OMG , you are years old so you were born in " with the correct values
print(f"OMG , you are {age_int} years old so you were born in {year_of_birth}")
# Second Part
# prompt the user for inputs and assign the variable age_int and name_str
# remove the initial values set
age_int = input("What is your age? ")
name_str = input("What is your name? ")
current_year = 2024
year_of_birth = int(current_year) - int(age_int)
# Third Part
# calculate and print out the total number of hours this person has lived
hours_lived = int(age_int) * 365 * 24

print(f"{name_str} has lived {hours_lived}hrs")
# If time
# figure out a way to account for if the persons birthday has already happened this year or not
birthday_this_year = input("Did your birthday take place already this year? (yes/no) ")
year_of_birth -= 1 if birthday_this_year == "no" else year_of_birth
print(f"OMG , you are {age_int} years old so you were born in {year_of_birth}")
# go look into the library 'time' to be more accurate with the hours lived

# show in your script that you have evaluated the methods of calculating the hours lived to see which is more accurate
# Acceptance Criteria
# program defines the variable age_int and name_str
# program prints the string "OMG , you are years old so you were born in "