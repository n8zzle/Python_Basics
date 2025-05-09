# Operators are used to perform opertaion on variables and values.

# Python divides the operators in the following groups:

# Arithmetic operators
# Addition -> + -> x + y
x = 5
y = 3
print("Addition: ", x + y)
# Substraction -> - -> x - y
x = 5
y = 3
print("Substraction: ", x - y)
# Multiplication -> * -> x * y
x = 5
y = 3
print("Multiplication: ", x * y)
# Division -> / -> x / y
x = 12
y = 3
print("Division: ", x / y)
# Modulus -> % -> x % y
x = 5
y = 2
print("Modulus: ", x % y)
# Exponentiation -> ** -> x ** y
x = 2
y = 5
print("Exponentiation: ", x**y)  # Same as 2*2*2*2*2
# Floor Division -> + -> x + y
x = 15
y = 2
print(
    "Floor Division: ", x // y
)  # The floor division // rounds the result down to the nearest whole number

# Assignment operators
# = -> x = 5
x = 5
print("x=5: ", x)

# += -> x+=3
x = 5
x += 3
print("x+=3: ", x)

# -= -> x-=3
x = 5
x -= 3
print("x-=3: ", x)

# *= -> x*=3 -> x = x * 3
x = 5
x *= 3
print("x*=3: ", x)

# /= -> x/=3 -> x = x / 3
x = 5
x /= 3
print("x/=3: ", x)

# %= -> x%=3 -> x = x % 3
x = 5
x %= 3
print("x%=3: ", x)

# //= -> x//=3 -> x = x // 3
x = 5
x //= 3
print("x//=3: ", x)

# **= -> x**=3 -> x = x ** 3
x = 5
x **= 3
print("x**=3: ", x)

# &= -> x&=3 -> x = x & 3
x = 5
x &= 3
print("x&=3: ", x)

# |= -> x|=3 -> x = x | 3
x = 5
x |= 3
print("x|=3: ", x)

# ^= -> x^=3 -> x = x ^ 3
x = 5
x ^= 3
print("x^=3: ", x)

# >>= -> x>>=3 -> x = x >> 3
x = 5
x >>= 3
print("x>>=3: ", x)

# <<= -> x<<=3 -> x = x << 3
x = 5
x <<= 3
print("x<<=3: ", x)

# := -> print(x:=3) -> x = 3; print(x)
x = 5
print("x:=3: ", x := 3)

# Comparison operators
# == -> Equal -> x==y
x = 5
y = 3
print("x == y: ", x == y)

# != -> Not Equal -> x!=y
x = 5
y = 3
print("x != y: ", x != y)

# > -> Greater than -> x>y
x = 5
y = 3
print("x > y: ", x > y)

# < -> Less than -> x<y
x = 5
y = 3
print("x < y: ", x < y)

# >= -> Greater than or equal to -> x>=y
x = 5
y = 3
print("x >= y: ", x >= y)

# <= -> Less than or equal to -> x<=y
x = 5
y = 3
print("x <= y: ", x <= y)

# Logical operators
# and
x = 5
print("x>3 and x<10: ", x > 3 and x < 10)

# or
x = 5
print("x > 3 or x < 4: ", x > 3 or x < 4)

# not
x = 5
print("not(x>3 and x<10): ", not (x > 3 and x < 10))

# Identity operators
# is
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print("x is z: ", x is z)  # True -> Because z is the same object as x
print(
    "x is y: ", x is y
)  # False -> Because x is not the same object as y, even if they have the same content
print("x == y: ", x == y)  # Just to show the difference between "is" and "=="

# is not
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print("x is not z: ", x is not z)  # False -> Because z is the same object as x
print(
    "x is not y: ", x is not y
)  # True -> Because x is not the same object as y,even if they have the same content
print("x != y: ", x != y)

# Membership operators
# in
x = ["apple", "banana"]
print("banana in x: ", "banana" in x)
# not in
x = ["apple", "banana"]
print("pineapple not in x: ", "pineapple" not in x)
