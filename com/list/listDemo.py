# list is the collection of data or items in single variable
# list follow the [] brackets
# list is a collection which is ordered and changeable. And allow the duplicates values

names = ['abir', 'yusuf', 'mim']
# print(len(names))

# names.reverse()
# print("Reverse the list: ")
# print(names)

# add new name end of the list
# names.append("madiha")
# print(names)

# insert the name based on the index number
# names.insert(0, "munni")
# print(names)

# removing the names from list
# del names[0]
# print(names)

# # sort, the method follow the alphabetically order
# names.sort()
# print(names)

# or reverse the list
# names.sort(reverse=True)
# print(names)


# Sorted
# print("Here is the orginal list: ")
# print(names)
# print("\nHere is the sorted list:")
# print(sorted(names))
#
# print("\nHere is the original list")
# print(names)
# range

# index
# y = names[0].title()
# print
# -1 always return the last item
# print(names[-1].title())

# TRY IT
# places = ['New York', 'Bangladesh', 'Switzerland', 'Paris', 'Denmark']
# print("Original list: ")
# print(places)
# print("\nHere is the sorted list: ")
# print(sorted(places))
# print("\nHere is the original list:")
# print(places)

# places.reverse()
# print(places)

# loop
for name in names:
    print("\nMy name is " + name.title())
# This loop will execute only once
print("Thank You, Everyone")
