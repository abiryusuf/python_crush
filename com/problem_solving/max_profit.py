# make a new list from two array list with order
# Or take two sorted lists and merge them to create a new sorted list
# compare two items then move to the next item

listA = [2, 8, 15, 23, 37]
listB = [4, 6, 15, 20]

def mergeSortedLists(listA, listB):
    newList = list()

    a = 0
    b = 0
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a += 1
        else:
            newList.append(listB[b])
            b += 1
    # if listA and listB contains more new items, append them to new list
    while a < len(listA):
            newList.append(listA[a])
            a += 1
    while b < len(listB):
            newList.append(listB[b])
            b += 1
    return newList

print(mergeSortedLists(listA, listB))


