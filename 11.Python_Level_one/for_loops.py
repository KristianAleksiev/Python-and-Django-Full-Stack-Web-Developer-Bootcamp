seq = [1, 2, 3, 4, 5, 6]
for item in seq:
    #block
    pass


dict = {
"Sam": 1,
"Frank": 2,
"Dan": 3,
}
for key in dict:
    print(key)
    print(dict[key])

for key in dict.keys():
    print(key)

for values in dict.values():
    print(values)

for key, value in dict.items():
    print(key, value)


my_pairs = [(1, 2), (3, 4), (5, 6)]
for item in my_pairs:
    print(item) # Gets the tuples
    print(my_pairs[item])

# Tuple unpacking
for (tup_first_element, tup_second_element) in my_pairs:
    print(tup_first_element) # First item in every tuple in the list
    print(tup_second_element) # Second item in every tuple in the list
