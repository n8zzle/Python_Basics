# You can loop through the list items by using a for loop:
thisList = ["Igors", "Cickalenko", 26, "Berlin"]

for x in thisList:
    print(x)

# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
thisList = ["apple", "banana", "cherry"]
for i in range(len(thisList)):
    print(thisList[i])

# Using while loop
thisList = ["test1", "test2", "test3"]
i = 0
while i < len(thisList):
    print(thisList[i])
    i = i + 1


# List Comprehension offers the shortest syntax for looping through lists:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
