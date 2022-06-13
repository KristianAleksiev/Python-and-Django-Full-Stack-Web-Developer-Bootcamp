def my_function(parameter="default"):
    """docstring as a multiline comment"""
    print("python function with {} parameter".format(parameter))

my_function()
print(my_function.__doc__)


def hello():
    return "Hello"
print(hello())


def add_num(number_one: int, number_two: int):
    if type(number_one) == type(number_two):
        return number_one + number_two
    return "Error"

x = add_num(5, 3)
print(x)


# Filter
my_list = [1, 2, 3, 4, 5, 6, 7, 8]

def even_bool(num):
    return num % 2 == 0

evens = filter(even_bool, my_list)
print(list(evens))

# Lambda expression
lambda num: num % 2 == 0
evens = filter(lambda num : num % 2 == 0, my_list) # (function, sequence)
print(list(evens))

# Check
list = [1, 2, 3, 4, 5, "x"]
boolean = "x" in list
print(boolean)
