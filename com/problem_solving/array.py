def common_elements(listA, listB):
    a = 0
    b = 0

    result = list()

    while a < len(listA) and b < len(listB):
        if listA[a] == listB[b]:
            result.append(listA[a] and result.append(listB[b]))
            a += 1
            b += 1
        elif listA[a] < listB[b]:
            a += 1
        else:
            b += 1
    return result


print((common_elements([1, 2, 4, 5, 6], [1, 3, 4, 6, 7])))


def common_element(a, b):
    num1 = 0
    num2 = 0

    result = []

    while num1 < len(a) and num2 < len(b):
        if a[num1] == b[num2]:
            result.append(a[num1]) and result.append(b[num2])
            num1 += 1
            num2 += 1
        elif a[num1] < b[num2]:
            num1 += 1
        else:
            num2 += 1

    return result


print((common_element([1, 3, 4, 5], [1, 2, 3, 4])))

def mergeSortedList(ListA, ListB):
    a = 0
    b = 0
    newList = list()

    seen = set()

    while a < len(ListA) and b < len(ListA):
        if ListA[a] < ListB[b]:
            newList.append(ListA[a])
            a += 1
        else:
            newList.append(ListB[b])
            b += 1
    # Add new item
    while a < len(ListA):
        newList.append(ListA[a])
        a += 1
    while b < len(ListB):
        newList.append(ListB[b])
        b += 1
    return newList
print(mergeSortedList([1, 2, 4, 7], [4, 5, 6, 8]))

list_1 = [1, 2, 3, 5]
list_2 = [1, 2, 5, 9]

x = list(list_1 + list_2)
print(sorted(x))



