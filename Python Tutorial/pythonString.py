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
test = "test String, to test Methods"
print(test.capitalize())  # Converts the first character to upper case
print(test.casefold())  # Converts string into lower case
print(test.center(100))  # Returns a centered string
# Returns the number of times a specified value occurs in a string
print(test.count("test"))
print(test.encode())  # Returns an encoded version of the string
# Returns true if the string ends with the specified value
print(test.endswith("Methods"))
print(test.expandtabs())  # Sets the tab size of the string
# Searches the string for a specified value and returns the position of where it was found
print(test.find("String"))
print(test.format())  # Formats specified values in a string
