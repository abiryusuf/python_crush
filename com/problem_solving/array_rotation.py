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
