# if __name__ == "__main__":
#     #code
#     pass


# __name__ - Built in variable
# which evaluates to the name of the current module
def function():
    print("function() in name_and_main.py")

print("Top level name_and_main.py")

if __name__ == '__main__':
    print("name_and_main.py is being run directly")
else:
    print("name_and_main.py has been imported")
