i = 1
while i < 5:
    print("i is {}".format(i))
    i += 1


list = list(range(0, 20, 2))
print(list)

list_two = range(5, 500) # Generator, less memory used
