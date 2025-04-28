# Python Add List items

# To add an item to the end of the list, use the append() method:
person = ["Igors", "Cickalenko"]
person.append(26)
print(person)

# To insert a list item at a specified index, use the insert() method.
person.insert(0, "Berlin")
print(person)

# To append elements from another list to the current list, use the extend() method.
thisList = ["apple", "banana", "cherry"]
tropicalList = ["mango", "pineapple", "papaya"]
thisList.extend(tropicalList)
print(thisList)
