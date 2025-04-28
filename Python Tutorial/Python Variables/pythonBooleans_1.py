# Booleans represent one of two values: True or False.
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Print a message base on whether the condition is True or False
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# The bool() function allows you to evaluate any value, and give you True or False
# Most values are True
print(bool("Hello"))
print(bool(15))
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
# Some values are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


# Example - Print "YES" if the function returns True, otherwise print "NO"


def myFunction():
    return True


if myFunction():
    print("YES!")
else:
    print("NO!")
