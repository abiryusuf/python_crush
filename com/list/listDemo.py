# list is the collection of data or items in single variable
# list follow the [] brackets
# list is a collection which is ordered and changeable. And allow the duplicates values

names = ['abir', 'yusuf', 'mim']
# print(len(names))

# add new name end of the list
# names.append("madiha")
# print(names)

# insert the name based on the index number
names.insert(0, "munni")
print(names)

# removing the names from list
# del names[0]
# print(names)

# sort, the method follow the alphabetically order
names.sort()
print(names)
# or reverse the list
names.sort(reverse=True)
print(names)

# range

# index
# y = names[0].title()
# print(y)

for name in names:
    print('\nMy name is ' + name.title())
