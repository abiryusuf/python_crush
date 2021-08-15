
arr = [1, 2, 3, 4, 5, 6, 7]

def arrayRotate(arr, target):
    n = len(arr)

    temp = []
    i = 0
    while i < target:
        temp.append(arr[i])
        i += 1
    i = 0
    while target < n:
        arr[i] = arr[target]
        i += 1
        target += 1
    arr_1 = arr[: i] + temp
    return arr_1
print(arrayRotate(arr, 3))

arr = [1, 4, 7, 8]


def rotation(list1, list2):
    if len(list1) != len(list2):
        return False
    key = list1[0]
    key_index = 0

    for i in range(len(list2)):
        if list2[i] == key:
            key_index = i
        break

    if key_index == 0:
        return False
    for x in range(len(list1)):
        index = (key_index + x) % len(list1)
        if list1[x] != list2[index]:
            return False
    return True
print(rotation([1, 2, 4, 5], [1, 2, 7, 8]))
