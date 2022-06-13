my_list = [1, 2, 3, 4, 5]
my_list = ["str1", "str2", 5, 3, 5.3, True, [1, 2, 3], {"key":"value"}]

len(my_list)
my_list[0] = "new item"
another_list = ["a", "b", "c"]

my_list.append("new last")
my_list.extend(another_list)

deleted_item = my_list.pop()
my_list.reverse()
my_list.sort()

my_list_two = [1, 2, ["x", "y", "z"]]
print(my_list_two[2][1])

# Comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
first_col = [element[0] for element in matrix]
print(first_col)


start = [1, 2, 3, 4]
finish = []
for num in start:
    finish.append(num ** 2)
print(finish)

finish = [num ** 2 for num in start]
