# LEGB Rule
# -Local - Assigned within an actual function
# -Enclosing function locals
# -Global
# -Built in

x = 25

def my_func():
    x = 35
    return x
### Local
lambda x: x ** 2

### Enclosing
name = "Global name"
def greet():
    name = "Georgi"
    def hello():
        print("hello " + name)
    hello()

greet()

### Global namespace
x = 50
def func():
    global x
    x = 1000
print(x)
func()
print(x)
