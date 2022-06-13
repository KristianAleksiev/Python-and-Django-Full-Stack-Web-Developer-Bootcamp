def array_check(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False

######

def string_bits(mystr):
    result = ""
    for i in range(len(mystr)):
        if i % 2 == 0:
            result += mystr[i]
    return result

######

def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return (b.endswith(a) or a.endswith(b))

######

def double_char(mystring):
    result = ""
    for char in mystring:
        result += char * 2
    return result

######

def no_teen sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if n [13, 14, 17, 19]: # In instruction
            retun 0
    return n

######

def count_evens(nums):
    count = 0
    for element in nums:
        if element % 2 == 0:
            count += 1
    return count
