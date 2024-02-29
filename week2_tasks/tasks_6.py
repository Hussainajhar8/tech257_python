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
