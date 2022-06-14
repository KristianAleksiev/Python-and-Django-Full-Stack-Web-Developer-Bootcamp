import re
# Finds patterns in text

patterns = ["term1", "term2"]

text = "This is a string with term1, not the other"

# for pattern in patterns:
#     print("I'm searching for: " + pattern)
#
#     if re.search(pattern, text):
#         print("Match!")
#     else:
#         print("No match!")

match = re.search("term1", text)
print(type(match))
print(match.start()) # The match starts at the index of

term = "@"
mail = "user@gmail.com"
print(re.split(term, mail))

# Find all
print(re.findall("match", "test phrase match in middle"))
print(re.findall("match", "test phrase match in middle and match in end"))


# Metacharacter Syntax
def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print()

#Repetition in a phrase
test_phrase = "sdsd..sssddd..sdddsddd...dsds...dssss...sdddd"
test_pattern = ["sd*"] # s followed by 0 or more d

multi_re_find(test_pattern, test_phrase)


test_pattern = ["sd+"] # s followed by 1 or more d
multi_re_find(test_pattern, test_phrase)

test_pattern = ["sd?"] # s followed by 0 or 1 time
multi_re_find(test_pattern, test_phrase)

test_pattern = ["sd{3}"] # s followed by 3 d
multi_re_find(test_pattern, test_phrase)

test_pattern = ["s[sd]+"] # s followed by either 1 or more s or 1 or more d
multi_re_find(test_pattern, test_phrase)

#Exclusion
test_phrase = "This is a string! But it has punctuation. How can we remove it?"
test_patterns = ["[^!.?]+"] # Removes the symbols (after [^....])
multi_re_find(test_pattern, test_phrase)

#Sequence of lower case characters
test_phrase = "This is a string! But it has punctuation. How can we remove it?"
test_patterns = ["[a-z]+"]
multi_re_find(test_pattern, test_phrase)

#Escape codes
test_phrase = "This is a string with numbers 1233123 and a symbol #hashtag"
test_patterns = [r"\d+"] #Search for digits
multi_re_find(test_pattern, test_phrase)

test_phrase = "This is a string with numbers 1233123 and a symbol #hashtag"
test_patterns = [r"\d+"] #Search for NON - digits
multi_re_find(test_pattern, test_phrase)

test_phrase = "This is a string with numbers 1233123 and a symbol #hashtag"
test_patterns = [r"\s+"] #Search for whitespaces
multi_re_find(test_pattern, test_phrase)

test_phrase = "This is a string with numbers 1233123 and a symbol #hashtag"
test_patterns = [r"\S+"] #Search for NON-whitespaces
multi_re_find(test_pattern, test_phrase)

test_phrase = "This is a string with numbers 1233123 and a symbol #hashtag"
test_patterns = [r"\w+"] #Search for alpha-numeric - numbers and letters
multi_re_find(test_pattern, test_phrase)

test_phrase = "This is a string with numbers 1233123 and a symbol #hashtag"
test_patterns = [r"\W+"] #Search for NON-alpha-numeric - spaces and symbols
multi_re_find(test_pattern, test_phrase)
