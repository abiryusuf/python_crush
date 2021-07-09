#
#
# def common_element(a, b):
#     num1 = 0
#     num2 = 0
#
#     result = []
#
#     while num1 < len(a) and num2 < len(b):
#         if a[num1] == b[num2]:
#             result.append(a[num1]) and result.append(b[num2])
#             num1 += 1
#             num2 += 1
#         elif a[num1] < b[num2]:
#             num1 += 1
#         else:
#             num2 += 1
#
#     return result
#
# print((common_element([1, 3, 4, 5], [1, 2, 3, 4])))
#
# def merge(a, b):
#     num_1 = 0
#     num_2 = 0
#
#     result = []
#
#     while num_1 < len(a) and num_2<len(b):
#         if a[num_1] == b[num_2]:
#             result.append(a[num_1]) and result.append(b[num_2])
#             num_1 += 1
#             num_2 += 1
#         elif a[num_1] < b[num_2]:
#             num_1 += 1
#         else:
#             num_2 += 1
#
#     return result

def reverse(str):

    res = ""

    for i in str:
        res = i + res
    return res
print(reverse("NIDHI"))

def prime(num):

    if num % 2 == 0:
        return "it is prime"
    else:
        "it is not prime "
print(prime(4))

def palindrome(str):
    new = ''
    reverse = ''

    for i in str:
        if i != "":
            new += i
            reverse = i + reverse
    if new == reverse:
        return "It is palindrome"
    else:
        return "it is not"

print(palindrome("abir"))