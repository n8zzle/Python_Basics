# List items are indexed and you can access them by referring to the index number:
thislist = ["apple", "banana", "cherry"]
# Apple
print(thislist[0])
# Banana
print(thislist[1])
# Cherry
print(thislist[2])

# Negative indexing means start from the end
print(thislist[-1])

# Range of indexes
fruitList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruitList[2:5])
# By leaving out the start value, the range will start at the first item:
print(fruitList[:4])
print(fruitList[2:])

if "kiwi" in fruitList:
    print("Yes, 'kiwi' is in the fruitlist")
