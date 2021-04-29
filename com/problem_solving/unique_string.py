# def unique_string(string):
#     string.replace(" ", "")
#     char = set()
#
#     for letter in string:
#         if letter in char:
#             return False
#         else:
#             char.add(letter)
#     return True
#
# def unique(string):
#     str = string.replace(" ", "")
#
#     return len(set(str)) == len(str)
#
# print(unique('abirr'))
# print(unique_string("a b c d"))

# def duplicate_value(num):
#
#     seen = set()
#     uniq = ""
#
#     for value in num:
#         if value not in seen:
#             uniq.append(value)
#             seen.add(value)
#     return uniq
#
# print(duplicate_value([1, 2, 2, 4, 3]))

# without set
def value(num):
    seen = {}
    dup = []

    for x in num:
        if x not in seen:
            seen[x] = 1
        else:
            if seen[x] == 1:
                dup.append(x)
            seen[x] += 1
    return dup
print(value([1, 2, 2, 3, 3, 4]))
