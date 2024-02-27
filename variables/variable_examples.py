a = 1
b = 2
c = 3.5
hi = "Hello world!"
y = a

print(type(a))
print(type(b))
print(type(c))
print(type(hi), "\n")

print("Before re-assign")
print("value of a:", a)
print(f"value of a: {a}")
print("ID of a:", id(a), "\n")

print("value of y:", y)
print(f"value of y: {y}")
print("ID of y:", id(y), "\n")

a = 10

print("After re-assign")
print("value of a:", a)
print(f"value of a:{a}")
print("ID of a:", id(a), "\n")

print("value of y:", y)
print(f"value of y: {y}")
print("ID of y:", id(y), "\n")