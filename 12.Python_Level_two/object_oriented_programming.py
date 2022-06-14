print(type([1, 2, 3]))

# Everything in python is an object

# class Sample():
#     pass
# x = Sample()
# print(x)

## Adding attributes(characteristics) and methods(functionality - operations) to my class

class Dog():

    # Class object attribute
    species = "mammal"

    def __init__(self, breed, name): # Attribute breed
        self.breed = breed #Value for attribute breed
        self.name = name



mydog = Dog(breed = "Rottweiler", name = "Doggo Edno")
my_otherdog = Dog(breed = "Cane corso", name = "Doggo Dve")
print(mydog)
print(mydog.breed)
print(my_otherdog.breed)
print(mydog.species)


class Circle():
    pi = 3.14

    def __init__(self, radius=1): # Default value of 1
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r


my_circle = Circle(3)
print(my_circle.radius)
print(my_circle.area())
# Changing the attribute value
# my_circle.radius = 5
my_circle.set_radius(5)
print(my_circle.area())

# INHERITANCE -> Base classes -> Derived classes

class Animal():


    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("Animal")
    def eat(self):
        print("EATING")

ani = Animal()
ani.who_am_i()
ani.eat()


class Dog(Animal):


    def __init__(self):
        # Animal.__init__(self)
        print("DOG CREATED")

    def bark(self):
        print("Wooof!")

    def eat(self):
        print("DOG EATING")


doggo = Dog()
doggo.who_am_i()
doggo.eat()
doggo.bark()

# SPECIAL METHODS

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

# my_book = Book("Python", "Jose", 200)
# print(my_book)
    def __str__(self): # String representation of the object
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

# my_book = Book("Python", "Jose", 200)
# print(my_book)
# print(len(my_book))

    def __len__(self):
        return self.pages

# my_book = Book("Python", "Jose", 200)
# print(len(my_book))

    def __del__(self):
        print("A book is destroyes")


my_book = Book("Python", "Jose", 200)
print(len(my_book))
del my_book
