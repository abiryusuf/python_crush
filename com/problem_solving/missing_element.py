def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
    return arr1[-1]

arr3 = [1, 3, 5, 6, 7]
arr4 = [1, 5, 6, 4, 6, 8]

print(finder(arr3, arr4))
