# Task: Using sets
# Objective
# Practice creating sets, adding and removing elements, and understanding the properties of sets.
#
# The task
# Explain 2 main ways that sets are different to lists and tuples
# 1. Uniqueness:
#    - Sets only contain unique elements; duplicates are automatically removed.
#    - Lists and tuples can contain duplicate elements without removal.
# 2. Ordering:
#    - Sets are unordered; the order of elements is not preserved.
#    - Lists and tuples maintain the order of elements as they are added or defined, respectively.

# Create a set named 'fruits' containing "apple", "banana", and "cherry".
fruits = {"apple", "banana", "cherry"}
# Print the set 'fruits'
print(fruits)
# Add "orange" to the fruits set using one of the set's methods.
fruits.add("orange")
# Print the set 'fruits' - check it's added
print(fruits)
# Remove "banana" from the fruits set using one of the set's methods.
# Print the set 'fruits' - check it's removed
fruits.remove("banana")
print(fruits)
# Attempt to add another "apple" to the fruits set.
# What do you observe? Stays the same
# Why does this happen? Sets only contain unique elements
fruits.add("apple")
# Print the final fruits set.
print(fruits)
# Print the 2nd item in the set. If there is any problem doing this, explain.
# Yes sets are unordered so indexing isn't possible