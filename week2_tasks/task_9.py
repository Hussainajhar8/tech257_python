#Task: Mix all the data about a user into a list

# Use your code from the "Task: Get name, age and DOB details from a user".
name_str = input("What is your name? ")
age_str = input("What is your age? ")
dob_str = input("What is your date of birth (DD/MM/YYYY)? ")

print(f"Hi {name_str}, you are {age_str} and your DOB is {dob_str}")

# Mix the name, age and DOB into one list user_details_list
user_details_list = [name_str, age_str, dob_str]

# Print the user's name, age and DOB from the list
print(user_details_list)

# Check the age is saved as an integer in the list. If it's not, work out how to convert it to an integer and add the age integer to the list.
print(type(user_details_list[1]))
user_details_list.insert(1, int(user_details_list[1]))
print(type(user_details_list[1]))

# Ask the user for their height in cm and save it to the variable height
height_str = input("What is your height in cm? ")

# Save height as a float in the list, and print the height from the list.
user_details_list.append(float(height_str))
print(user_details_list[4])
print(type(user_details_list[4]))