# arr = [20, 3, 2, 1, 5, 4]
#
# def sum(num):
#     total = 0
#     n = len(num)
#     for i in num:
#         total += i
#     return total
# print(sum(arr))
#
#
# # Total with dictionary
#
# groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99,
#  "bread": 4.59, "coffee": 6.99, "milk": 3.39, "eggs": 2.98,
#  "cheese": 5.44}
#
# def total(num):
#     sum = 0
#     for i in num:
#         sum += num[i]
#     return round(sum, 2)
# print(total(groceries))
#
# def maxNumber(num):
#     max = 0
#     n = len(num)
#     for i in range(0, n):
#         current = num[i]
#         if current > max:
#             max = current
#     return max
# print(maxNumber(arr))
#
# def factorial(num):
#     res = 1
#
#     for i in range(1, num + 1):
#         res = res * i
#     return res
# print(factorial(5))
#
#
# duplicate = [2, 2, 3, 4, 4, 6, 6]
# def duplicateNum(num):
#     unique = []
#     seen = set()
#     for value in num:
#         if value not in seen:
#             unique.append(value)
#             seen.add(value)
#     return unique
# print(duplicateNum(duplicate))

# def countVowels(str):
#     res = 0
#     str = str.replace(" ", "").lower()
#
#     for char in str:
#         if char in "aeiou":
#             res = res + 1
#     return res
#
# print(countVowels("abir yUsuf"))
#
#
# groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99,
#  "bread": 4.59, "coffee": 6.99, "milk": 3.39, "eggs": 2.98,
#  "cheese": 5.44}
#
# number = [2, 5, 8, 9]
# def sum(num):
#     total = 0
#     for i in num:
#         total += num[i]
#     return round(total, 2)
# print(sum(groceries))
#
# def factorial(num):
#     res = 1
#     for i in range(1, num + 1):
#         res = res * i
#     return res
# print(factorial(5))
#
# # for c in range(1, 6, 2):
# #     print(c)
#
# def total(num):
#     sum = 0
#
#     for i in range(1, num + 1):
#         sum += i
#     return sum
# print(total(5))
#
# num = [2, 5, 6]
#
#
# def maxNum(num):
#     max = 0
#     n = len(num)
#     for x in range(n):
#         current = num[x]
#         if current > max:
#             max = current
#     return max
# print(maxNum(num))

# arrList = [3, 20, 10, 5, 7, 8]
# def findMin(num):
#     length = len(num)
#     number = sorted(num)
#
#     min = number[0]
#
#     for i in range(1, length):
#         if number[i] < min:
#             min = number[i]
#     return min
# print(findMin(arrList))

num = [5, 7, 8, 14, 11, 10]


num.sort()
print(num)

num.sort(reverse=True)
print(num)

thisList = ["apple", "banana", "cherry"]
myList = thisList
print(myList)
