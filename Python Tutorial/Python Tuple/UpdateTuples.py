# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

# Updating Tuples
# Converting Tuple into list to be able to update values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Adding items
x = ("Igors", "Cickalenko")
y = list(x)
y.append(26)
x = tuple(y)
print(x)

# Removing items
x = ("Igors", "Cickalenko", "Berlin", 26)
y = list(x)
y.remove(26)
x = tuple(y)
print(x)

# Completely removing tuple
x = ("Igors", "Cickalenko", "Berlin", 26)
del x
