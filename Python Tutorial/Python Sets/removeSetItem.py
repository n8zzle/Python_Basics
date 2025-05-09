# To remove an item in a set, use the remove(),
# or the discard() method.

thisSet = {"Igors", "Cickalenko", 26, "Berlin"}
thisSet.remove("Berlin")
# OR
thisSet.discard(26)
print(thisSet)

# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.
thisSet = {"Igors", "Cickalenko", 26, "Berlin"}
thisSet.pop()
print(thisSet)

thisSet = {"Igors", "Cickalenko", 26, "Berlin"}
thisSet.clear()
print(thisSet)
