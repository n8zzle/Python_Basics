import random

# There are three numeric types in Python:
# int
# float
# complex

x = 1  # int
print(type(x))
y = 2.8  # float
print(type(y))
z = 1j  # complex
print(type(z))

# Integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Float, number with decimal
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# Complex numbers are written with a "j"
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Type Conversion
x = 1
y = 2.8
z = 1j

# Convert from int to float
a = float(x)
# Convert from float to int
b = int(y)
# Convert from int to complex
c = complex(x)

print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

# Random number
print("Random Number : ", random.randrange(1, 10))
