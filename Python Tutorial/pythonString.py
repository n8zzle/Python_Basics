# String Slicing
b = 'Hello World!'
print(b[2:7])
# Slice from the Start
print(b[:5])
# Slice to the End
print(b[2:])
# Negative Indexing -- to start the slice from the end
print(b[-5:-2])


# Modify Strings
a = "   My name is Igors.   "
# Upper Case
print(a.upper())
# Lower Case
print(a.lower())
# Remove whitespace
print(a.strip())
# Replace
print(a.replace("Igors", "Max"))
# Split
print(a.split("is"))
a2 = a.split("is")[1]
print(a2)

# Concatenate Strings
print(a + "" + a2)

# F-Strings
age = 26
txt = f"My name is Igors, I am {age}"
print(txt)
# Is ok , but better to use f-string
print("My name is Igors, I am", age)
