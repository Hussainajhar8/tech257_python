# TASK: Waiter Helper
# Rationale: To practice lists
# Script should act like a waiter at a restaurant taking orders

# level 1

# Greet the user
print("Hi , welcome to our restaurant, please have a look at our menu and let me know if you need any help")

# Print a list of starters
starters = ["wings", "fries", "chicken_popcorn", "chicken_strips", "garlic_bread"]
print(f"Listed are the starters: {starters}")
# Take an input for the user for their starter
starter = input("What would you like to have for starters? ")
# Print a list of mains
mains = ["chicken_burger","quarter_pounder","pizza"]
print(f"Listed are the mains: {mains}")
# Take an input for the user for their main course
main = input("What would you like to have for your main? ")
# Print a list of desserts
desserts = ["apple_pie", "chocolate_fudge_cake", "icecream"]
print(f"Listed are the desserts: {desserts}")
# Take an input for the user for their dessert
dessert = input("What would you like to have for dessert? ")
# Print all of the user's choices
print(f"Starter:{starter}, Main:{main}, Dessert:{dessert}")
# level 2
# Use at least one f-string
# Add each item ordered to a list called 'customer_order_list'
customer_order_list = [starter, main, dessert]
# if time: level 3 (may need research if we have not covered dictionaries yet)
# Use dictionaries and assign prices to the items. Create a bill at the end of the program.
# menu = {
#     starters: ["£2.50", "£1.50", "£2.00", "£2.50"],
#     mains: ["£3.00", "£3.00", "£4.00"],
#     desserts: ["£1.00", "£1.50", "£1.00"]
# }
# print(menu)
# if time: level 4
# Add more to this program. Recommended ways are: Only allow input that is within the list, Add quantities of order etc.