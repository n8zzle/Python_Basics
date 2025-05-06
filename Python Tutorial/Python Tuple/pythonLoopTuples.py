# You can loop through the tuple items by using a for loop.
admin = ("Igors", "Cickalenko", 26, "Berlin", True, "BMW", "335d", "313PS")
for i in admin:
    print(i)

# You can also loop through the tuple items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
admin = ("Igors", "Cickalenko", 26, "Berlin", True, "BMW", "335d", "313PS")
for i in range(len(admin)):
    print(admin[i])

# Using While loop
admin = ("Igors", "Cickalenko", 26, "Berlin", True, "BMW", "335d", "313PS")
i = 0
while i < len(admin):
    print(admin[i])
    i = i + 1
