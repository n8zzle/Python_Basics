# Lists are used to store multiple items in a single variable.
mylist = ["apple", "banana", "cherry"]
print(mylist)

# To determine how many items a list has, use the len() function:
print(len(mylist))

# String List
list1 = ["apple", "banana", "cherry"]
# Int List
list2 = [1, 5, 7, 9, 3]
# Boolean List
list3 = [True, False, False]
# Mixed List
list4 = ["apple", 1, True]

# From the Python perspective , lists are defined as objects with the data type 'list':
print(type(list4))

# It is also possible to use the list() constructor when creating a new list.
thisList = list(["test1", "test2", "test3"])
print(thisList)
