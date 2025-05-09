# Set items are unordered, unchangeable, and do not allow duplicate values.
# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

myset = {"Igors", "Cickaleno", 26}
print(myset)

# Duplicates Not Allowed
# Sets cannot have two items with the same value.
# Duplicated will be ignored.
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# TODO: The values True and 1 are considered the same value in sets, and are treated as duplicates
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# TODO: The values False and 0 are considered the same value in sets, and are treated as duplicates
thisset = {"apple", "banana", "cherry", False, 0, 2}
print(thisset)

# Get a length of the set
print(len(thisset))

# Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)
