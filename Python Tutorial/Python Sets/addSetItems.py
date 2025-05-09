# Once a set is created, you cannot change its items,
# but you can add new items.

# To add one item to a set use the add() method.

thisSet = {"Igors"}
thisSet.add("Cickalenko")
thisSet.add("Berlin")
thisSet.add(26)

print(thisSet)


# To add items from another set into the current set, use the update() method.
thisSet = {"Igors", "Cickalenko", "Berlin", 26}
dreamCarSet = {"BMW", "M3", "F80"}
thisSet.update(dreamCarSet)
print(thisSet)

# The object in the update() method does not have to be a set,
# it can be any iterable object (tuples, lists, dictionaries etc.)
thisSet = {"Igors", "Cickalenko", "Berlin", 26}
myList = ["BMW", "M3", "F80", "from 2014"]
thisSet.update(myList)
print(thisSet)
