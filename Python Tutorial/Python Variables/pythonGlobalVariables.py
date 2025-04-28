# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

x = "Awesome"


def myFunc():
    print("Python is " + x)


myFunc()

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
y = "Super"


def newFunc():
    y = "Fantastic"
    print("Python is " + y)


newFunc()
print("Python is " + y)

# To create a global variable inside a function, you can use the global keyword
# To change the value of a global variable inside a function, refer to the variable by using the global keyword
user = "Anonymous"


def globalFunc():
    global user
    user = "Cickalenko Igors"


globalFunc()
print("User: " + user)
