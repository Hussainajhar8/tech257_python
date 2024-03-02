# TASK: Fizz Buzz!

# Print incremented numbers to the screen but substitute multiples of 3 with 'Fizz', multiples of 5 with 'Buzz', and multiples of both with 'FizzBuzz'
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz" instead of the number
# For numbers which are multiples of both three and five print "FizzBuzz".
#
number = 1
while number < 101:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    number += 1

#
# If time:
#
# Improve the script so we can decide which numbers to substitute for "Fizz" and "Buzz"
print()

number = 1
fizz_number = input("what number should print 'Fizz' if its a factor? ")
buzz_number = input("what number should print 'Buzz' if its a factor? ")

while number < 101:
    if number % int(fizz_number) == 0 and number % int(buzz_number) == 0:
        print("FizzBuzz")
    elif number % int(fizz_number) == 0:
        print("Fizz")
    elif number % int(buzz_number) == 0:
        print("Buzz")
    else:
        print(number)
    number += 1
print()
# Refactor using functions
def fizzbuzz(range1,range2):
    print("function works!")
    number = range1
    fizz_number = input("what number should print 'Fizz' if its a factor? ")
    buzz_number = input("what number should print 'Buzz' if its a factor? ")

    while number < range2:
        if number % int(fizz_number) == 0 and number % int(buzz_number) == 0:
            print("FizzBuzz")
        elif number % int(fizz_number) == 0:
            print("Fizz")
        elif number % int(buzz_number) == 0:
            print("Buzz")
        else:
            print(number)
        number += 1

fizzbuzz(0,15)

# Acceptance Criteria
# All core task are done
# Core works with no errorop