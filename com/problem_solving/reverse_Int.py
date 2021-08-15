arr = [1, 2, 3, 4]
list_1 = 1, 2, 3, 4
for i in reversed(arr):
    print(i, end=" ")

x = list_1[::-1]
print("\n")
print(x)


def reverseInt(int):
    size = len(int)

    res = []
    for index in range(size):
        size -= 1
        res.append(int[size])
    return res
print(reverseInt(list_1))