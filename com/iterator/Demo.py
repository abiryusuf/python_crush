"""
An iterator is an object that contains a countable number of values
Meaning that i can traverse through the all values

using two methods iter() and next()
"""

myList = [1, 2, 3, 4, 5]

x = iter(myList)
print(next(x))
print(next(x))
# for i in x:
#     print(i)

yusuf = {
    "name" :" abir",
    "name": "yusuf",
    "place": "Ny"
}

print(yusuf)


for i in myList:
    if i % 2 == 0:
        print(str(i) + " Is an even number")
    else:
        print(str(i) + " Is an odd number")
