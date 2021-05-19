# def linear(value, target):
#     length = len(value)
#     for i in range(0, length):
#         if value[i] == target:
#             return i
#     return - 1
#
# arr = [2, 4, 6, 8, 9]
# target_value = 6
#
# x = linear(arr, target_value)
# if x == -1:
#     print("Item is not found")
# else:
#     print("Item is found", x)
#
#
# def smallest_num(num):
#
#     length = len(num)
#     smallest = num[0]
#
#     for i in range(1, length):
#         if num[i] < smallest:
#             smallest = 0
#     return smallest
# x = smallest_num(arr)
# print("Smallest Number " + str(x))
#
#
# def largest_num(num):
#     length = len(num)
#     max = 0
#     for i in range(1, length):
#         if num[i] > max:
#             max = num[i]
#     return max
# print(largest_num(arr))


def binary_search(value, target):
    low = 0
    high = len(value) - 1

    while low <= high:
        mid = (low + high) // 2
        if value[mid] == target:
            return True
        elif target < value[mid]:
            high = mid
        else:
            low = mid
    return False

arr = [3, 5, 6, 8, 9, 10]
target_value = 8

x = binary_search(arr, target_value)
if x == -1:
    print("Not found")
else:
    print("Item is found", x)

# check balance

def check_balance(s):
    if len(s) % 2 == 0:
        return True

    stack = []
    opening = set('([{')
    matching = set([('(', ')'), ('[', ']'), ('{', '}')])

    for parent in s:
        if parent in opening:
            stack.append(parent)
        else:
            if len(s) == 0:
                return False
            last_open = stack.pop()
            if (last_open, parent) not in matching:
                return False
    return len(stack) == 0
print(check_balance("()"))


