# Task: Using frozen sets

# The task
# Create a frozen set named frozen_set containing elements "hello", "world".
frozen_set = frozenset(["hello", "world"])
print(frozen_set)
print(type(frozen_set))

# Try to add "!" to frozen_set. What happens?
# frozen_set.add("!") # - results in error  AttributeError: 'frozenset' object has no attribute 'add'

# Create a normal set named normal_set containing elements "let's", "learn".
normal_set = {"let's", "learn"}
# Try to add frozen_set to normal_set. Why does it work? Explain.
normal_set.add(frozen_set)
# Print normal_set.
print(normal_set)
# Run your script half a dozen times. What do you notice about where frozen_set is added to normal_set? Hint: Look at the order of the items.
# The order of the values changes because sets are unordered
# What makes a frozen set different to a normal set? Explain.
# The frozenset() function returns an unchangeable frozenset object (which is like a set object, only unchangeable).