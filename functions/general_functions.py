def print_something(print_string):
    print(print_string)

print_something("hello")

def addition(number1=1, number2=2) -> int:
    return number1 + number2

def multi_args(*multiargs):
    print(type(multiargs))
    for arg in multiargs:
        print(arg)


def greeting(name: str):
    print("Hello, my name is " + str(name))

greeting(2002)

print(addition(5, 10))
print(addition())

multi_args(1, 2, "hello", ["1", "2"])