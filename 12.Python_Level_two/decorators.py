# Advanced tool in python
# Functions which modify the functionality of other Functions
s = "GLOBAL VARIABLE"
def func():
    my_local = 10
    print(locals()) # => Returns dictionary type
    print(globals()) # Returns the globals built-ins included
    print(globals()["s"])
func()

print(func())


def hello(name="Kristian"):
    return "hello " + name
print(hello())

my_new_greet = hello
print(my_new_greet())
####################################

def hello_again(name="Kristian")
    print("THE HELLO_AGAIN() FUNCTION HAS BEEN RUN!")

    def greet():
        return "INSIDE GREET()"

    def welcome():
        return "INSIDE WELCOME()"

    # print(greet())
    # print(welcome())
    # print("END OF HELLO_AGAIN()")
    if name == "Kristian": # RETURNING A FUNCTION
        return greet
    else:
        return welcome

x = hello_again()
print(x())

# FUNCTION AS AN ARGUMENT

def hi():
    return "Hi Kristian"

def other(func):
    print("HELLO")
    print(func()) # Calling it inside a function

other(hi)

# CREATING A DECORATOR

def new_decorator(func):
    def wrap_func():
        print("Code here before executing func")
        func()
        print("FUNC() has been called")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a decorator!")

# func_needs_decorator = new_decorator(func_needs_decorator)
# func_needs_decorator()
@new_decorator
def func_needs_decorator():
    print("This function is in need of a decorator!")

func_needs_decorator()
