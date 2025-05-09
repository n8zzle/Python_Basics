# Unpacking Tuple
admin = ("Igors", "Cickalenko", 26, "Berlin", True, "BMW", "335d", "313PS")

(name, surname, age, city, isAdmin, autoMarke, autoModel, autoHP) = admin

print(name)
print(surname)
print(age)
print(city)
print(isAdmin)
print(autoMarke)
print(autoModel)
print(autoHP)

# Using Asterisk - *
# If the number of variables is less than the number of values,
# you can add an * to the variable name and the values will be assigned to the variable as a list:
admin = ("Igors", "Cickalenko", 26, "Berlin", True, "BMW", "335d", "313PS")

(name, surname, *etc) = admin

print(name)
print(surname)
print(etc)

# If the asterisk is added to another variable name than the last,
# Python will assign values to the variable until the number of values left matches the number of variables left.
admin = ("Igors", "Cickalenko", 26, "Berlin", True, "BMW", "335d", "313PS")

(name, *etc, autoHP) = admin

print(name)
print(etc)
print(autoHP)
