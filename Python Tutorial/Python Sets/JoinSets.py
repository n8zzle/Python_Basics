# Union
# The union() method returns a new set with all items from both sets.
firstSet = {"Igors", "Cickalenko", 26, "Latvia", "Jekabpils"}
secondSet = {"Ilze", "Dubova", 26, "Latvia", "Kraslava"}
result = firstSet.union(secondSet)
print(result)

# You can use the | operator instead of the union() method, and you will get the same result
firstSet = {"Igors", "Cickalenko", 26, "Latvia", "Jekabpils"}
secondSet = {"Ilze", "Dubova", 26, "Latvia", "Kraslava"}
result = firstSet | secondSet
print(result)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)

# The union() method allows you to join a set with other data types, like lists or tuples.
# The result will be a set.
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

# Intersection
# Keep ONLY the duplicates
# The intersection() method will return a new set, that only contains the items that are present in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

# You can use the & operator instead of the intersection() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

# You can use the - operator instead of the difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

# Use the difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
