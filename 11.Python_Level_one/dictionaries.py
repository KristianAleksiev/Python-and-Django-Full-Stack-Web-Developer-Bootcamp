my_dict = {
"key_one": 1,
"key_two": 2.0,
"key_three":"value_three",
"key_four": [1, 2, "Get me"]
}
print(my_dict["key_one"])
print(my_dict["key_four"][2].upper())

dict_two = {
"lunch":"pizza",
"breakfast": "eggs",
}
dict_two["breakfast"] = "steak"
print(dict_two)
dict_two["dinner"] = "salad"
print(dict_two)
