# Python allows you to assign values to multiple variables in one line
x, y, z = "Apple", "Cherry", "Banana"
print("X:", x, "Y:", y, "Z:", z)

# Also you can assign the same value to multiple variables in one line
x = y = z = "Orange"
print("X:", x, "Y:", y, "Z:", z)

# If you have a collection of values in a list. Python allows you to extract the values into variables. This called unpacking. 
fruits = ["Apple", "Watermellon", "Strawberry"]
x, y, z = fruits
print("X:", x, "Y:", y, "Z:", z)
