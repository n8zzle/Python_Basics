# String Slicing
b = "Hello World!"
print(b[2:7])
print(b[:5])  # Slice from the Start

print(b[2:])  # Slice to the End

print(b[-5:-2])  # Negative Indexing -- to start the slice from the end


# Modify Strings
a = "   My name is Igors.   "
print(a.upper())  # Upper Case
print(a.lower())  # Lower Case
print(a.strip())  # Remove whitespace
print(a.replace("Igors", "Max"))  # Replace
print(a.split("is"))  # Split
a2 = a.split("is")[1]
print(a2)

print(a + "" + a2)  # Concatenate Strings


# F-Strings
age = 26
txt = f"My name is Igors, I am {age}"
print(txt)
print("My name is Igors, I am", age)  # Is ok , but better to use f-string


# Text Characters
# \' - Single Quote
# \\ - Backslash
# \n - New Line
# \r - Carriage Return
# \t - Tab
# \b - Backspace
# \f - Form Feed
# \ooo - Octal value
# \xhh - Hex value

# String Methods

# Capitalize method - Capitalize the first letter in this sentence
txt = "hello, and welcome to my world"
x = txt.capitalize()
print("Capitalize method: " + x)

# Casefold method - Make the string lower case.
txt = "Hello , And Welcome To My World"
x = txt.casefold()
print("Casefold method: " + x)

# Center method - taking up the space
txt = "banana"
x = txt.center(30)
print("Center method: " + x)

# Count method - Return the number of times the value appears in the string
txt = "I love apples, appe are my favorite fruit."
x = txt.count("apple")  # Returns as number
print("Count method: " + str(x))

# Encode method - UTF-8 encode the string
txt = "My name is Ståle"
x = txt.encode()
print("Encode method: ", x)

# Endswith method - Check if the string ends with punctuation sign (.)
txt = "Hello , welcome to my world."
x = txt.endswith(".")
print("Endswith method: ", x)

# Expandtabs method - Set the tab size
txt = "H\te\tl\tl\to"
x = txt.expandtabs(5)
print("Expandtabs method: ", x)

# Find Method - finds the specified value. Returns -1 if the value is not found
txt = "Hello , welcome to my world."
x = txt.find("welcome")
print("Find method: ", x)

# Format method - Insert specidied values inside the string
txt = "For only {price} euro!"
print("Format method: ", txt.format(price=49))

# Index method - find the first occurrence of the value
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print("Index method: ", x)

# Join method - takes all items in an iterable and joins them into one string.
myTuple = ("John", "Peter", "Vicky", "Igors", "Max", "Ilze")
x = "|".join(myTuple)
print("Join method: ", x)

# ljust method - will left align the string
txt = "banana"
x = txt.ljust(20)
print("ljust method: ", x, "is my favorite fruit.")

# lower method - returns lower case string
txt = "Hello my FRIENDS"
x = txt.lower()
print("Lower method: ", x)

# lstrip method - removes any leading characters (space is the default leading character)
# In this example it will remove spaces from the left side
txt = "      banana      "
print("lstrip method: ", txt.lstrip(), "is my favorite")

# maketrans method
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print("Maketrans method:", txt.translate(mytable))

# Partition method
# Search for the word "bananas", and return a tuple with three elements:
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print("Partition method: ", x)
print("Partition method [everything before the match]: ", x[0])
print("Partition method [match]: ", x[1])
print("Partition method [everything after the match]: ", x[2])

# Replace method
txt = "i like bananas"
x = txt.replace("bananas", "apples")
print("Replace method: ", x)

# Split method - split a string into a list.
txt = "welcome to the jungle"
x = txt.split()
print("Split method: ", x)

# title method - returns each word first letter in upper case
txt = "Welcome to my world"
x = txt.title()
print("Title method: ", x)

# Translate method - returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.
# Use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83: 80}
txt = "Hello Sam!"
print("Translate method: ", txt.translate(mydict))

# Zfill method - adds zeros (0) at the beginning of the string, until it reaches the specified length.
txt = "50"
x = txt.zfill(10)
print("Zfill method: ", x)
