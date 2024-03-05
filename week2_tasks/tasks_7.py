print("\nTask 7 - Task: Calculate Year of Birth")
# First part
# define the variables age_int and name_str (set dummy/default/initial values)
age_int = 23
name_str = "Ramon"
current_year = 2024
# make a calculation for the year in which the person was born
year_of_birth = current_year - age_int
# print out "You are years old so you were born in " with the correct values
print(f"You are {age_int} years old so you were born in {year_of_birth}")
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
print(f"You are {age_int} years old so you were born in {year_of_birth}")
# go look into the library 'time' to be more accurate with the hours lived

# show in your script that you have evaluated the methods of calculating the hours lived to see which is more accurate
# Acceptance Criteria
# program defines the variable age_int and name_str
# program prints the string "OMG , you are years old so you were born in "