s = "django"
print(s[0])
print(s[-1])
print(s[:4])
print(s[1:4])
print(s[-2:])
print(s[::-1])

nested_list = [3, 7, [1, 4, "hello"]]
switch = nested_list[2][2] = "goodbye"
print(switch)

d_one = {"simple_key": "hello"}
print(d_one["simple_key"])

d_two = {"k1":{"k2": "hello"}}
print(d_two["k1"]["k2"])

d_three = {"k1":[{"nest_key": ["this is deep", ["hello"]]}]}
print(d_three["k1"][0]["nest_key"][1])

my_list = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3]
my_list = set(my_list)
print(my_list)

age = 4
name = "Sammy"
print("Hello my dog's name is {} and he is {} years old.".format(name, age))
