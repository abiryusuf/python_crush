def linear(value, target):
    length = len(value)
    for i in range(0, length):
        if value[i] == target:
            return i
    return - 1

arr = [2, 4, 6, 8, 9]
target_value = 6

x = linear(arr, target_value)
if x == -1:
    print("Item is not found")
else:
    print("Item is found", x)


def smallest_num(num):

    length = len(num)
    smallest = num[0]

    for i in range(1, length):
        if num[i] < smallest:
            smallest = 0
    return smallest
x = smallest_num(arr)
print("Smallest Number " + str(x))


def largest_num(num):
    length = len(num)
    max = 0
    for i in range(1, length):
        if num[i] > max:
            max = num[i]
    return max
print(largest_num(arr))

