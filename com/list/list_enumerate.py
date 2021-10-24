# what if you want to access the elements in a list,
# along with the index of the element in question?
# You can do this using the enumerate () function.
# The enumerate () function takes a list as a parameter
# and returns a tuple for each element in the list.
# The first value of the tuple is the index,
# and the second value is the element itself.

winner = ['Abir', 'Yusuf', 'Mim', 'Madiha']

for index, person in enumerate(winner):
    print("{}. - {}".format(index + 1, person))

thisList = ["apple", "banana", "cherry"]

theList = ["mango", "papaya"]

thisList.extend(theList)
print(thisList)

thisList.pop()
print(thisList)


add = []

# for i in range(1, 20):
#     add.append(i - 2)
# print(add)

def convertToDic(str):
    str = str.split()

    for inx, value in enumerate(str):
        return "Index {} and value {}".format(inx, value)
print(convertToDic("gfg*is*best*for*geeks"))
