
test_str = 'gfg_is_best_for_geeks'

print(str(test_str))

delim = "_"

x = test_str.split(delim)
res = {}

for idx, ele in enumerate(x):
    res[idx] = ele

print(res)

def String_to_Dict(str):
    y = "_"
    x = str.split(y)
    res = {}

    for i, ele in enumerate(x):
        res[i] = ele
    return res
print(String_to_Dict(test_str))


list_1 = ["Abir", "Yusuf", "Mim"]
def list_to_dict(list):

    res = {}

    for i, ele in enumerate(list):
        res[i + 1]= ele
    return res
print(list_to_dict(list_1))


num = [5, 8, 10, 12, 3]

def largest(n):
    min = n[0]
    length = len(n)
    for i in range(1, length):
        current = n[i]
        if current < min:
            min = current
    return min
print(largest(num))


def swapList(newList):
    size = len(newList)

    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList


# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))

def swap(listNew):
    size = len(listNew)

    first = listNew[0]
    listNew[0] = listNew[size-1]
    listNew[size - 1] = first

    return listNew

print(swap(newList))


for num in range(100, 200):
    # if all(num % i != 0 for i in range(2, num)):
    #     print(num)
    if num % 2 == 0:
        print("Prime Number: " + str(num))

