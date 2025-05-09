list = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list + list2
print(list3)

list = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list:
    list2.append(x)
print(list2)

list = ["a", "b", "c"]
list2 = [1, 2, 3]
list2.extend(list)
print(list2)
