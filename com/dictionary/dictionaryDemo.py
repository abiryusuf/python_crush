# Dictionaries are used to store data in key : value paries
# It doesn't allow the duplicate values and it changeable

# info = {
#     "Name": "Abir",
#     "Age": 32,
#     "Address": "NY"
# }
# print(info)
#
# # index
# x = info["Name"]
# print(x)
#
# # check with key
# y = "Name" in info
# print(y)
#
# doc = {"Introduction": 1, "Chapter 1": 4, "Chapter 2": 11, "Chapter 3": 25, "Chapter 4": 30}
#
# # add
# doc["Chapter 8"] = 49
# print(doc)
#
# # change
# doc["Chapter 8"] = 50
# print(doc)

# using item() method
file_counts = {"jpg": 10, "text": 14, "csv": 2, "py": 23}

for ext, amount in file_counts.items():
    print("There are {} files with the .{} extention ".format(ext, amount))

personal_info = {"abir": 30, "mim": 5, 'madiha': 2}

for name, age in personal_info.items():
    print("My name is {} and I am {} years old".format(name.title(), age))

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}

for key, value in cool_beasts.items():
    print("{} have {}".format(key, value))

# count letters
def count_letter(text):
    txt = text.replace(" ", "").lower()
    res = {}

    for letter in txt:
        if letter in res:
            res[letter] += 1
        else:
            res[letter] = 1
    return res
print(count_letter("I am abir"))


# def count_word(n):
#     x = n.split(" ").lower()
#     res = {}
#     for word in x:
#         if word in res:
#             res[word] += 1
#         else:
#             res[word] = 1
#     return res
#
# print(count_letter("I am abir"))

# range
aliens = []
for alien in range(20):
    new_aliens = {"color": "Green", "point": 4, "Speed": "slow"}
    aliens.append(new_aliens)

for alien in aliens[:10]:
    print(alien)
