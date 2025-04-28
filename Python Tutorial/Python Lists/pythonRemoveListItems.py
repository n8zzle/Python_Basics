# The remove() method removes the specified item.
thisList = ["Igors", "Cickalenko", 26, "Berlin"]
thisList.remove("Berlin")
print(thisList)

# The pop() method removes the specified index
thisList = ["Igors", "Cickalenko", 26, "Berlin"]
thisList.pop(2)
print(thisList)

# If you do not specify the index, the pop() method removes the last item.
thislist = ["igors", "cickalenko", 26, "berlin"]
thislist.pop()
print(thislist)

# The del also removes specified index
thisList = ["Igors", "Cickalenko", 26, "Berlin"]
del thisList[0]
print(thisList)
# Also can delete the list completely
thisList = ["Igors", "Cickalenko", 26, "Berlin"]
del thisList

# the clear() method empties the list
thisList = ["igors", "cickalenko", 26, "berlin"]
thisList.clear()
print("Clear list: ", thisList)
