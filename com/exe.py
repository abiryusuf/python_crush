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

# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
#
# new_files = []
#
# for name in filenames:
#     if name.endswith(".hpp"):
#         name = name.replace(".hpp", ".h")
#         new_files.append(name)
#     else:
#         new_files.append(name)
# print(new_files)

# arr = [4, 2, 6, 8, 1, 9]
#
# length = len(arr)
# max = 0
#
# for i in range(1, length):
#     if arr[i] > max:
#         max = arr[i]
# print(max)
#
# min = arr[0]
# for i in range(1, length):
#     arr[i]
#     if arr[i] < min:
#         min = arr[i]
# print(min)
# mul = 1
# for i in range(1, length):
#     arr[i]
#     mul = mul * arr[i]
# print(mul)
#
# x = 1
# for i in range(1, 5 + 1):
#     x = x * i
# print(x)
# swap
# a = 4
# b = 5
# x = a
# a = b
# b = x
#
# print(a, b)
# import math as x
# arr = [3, 5, 7, 8]
# print(x.fsum(arr))
# print(x.log(2))
 # x = int(input("Enter number: "))
# def ifElse(a, b):
#     if a > b:
#         return "A is greater than B"
#     elif a < b:
#         return "B is greater than A"
#     elif a == b:
#         return "A and B is equal"
#     else:
#         return "Nothing"
# print(ifElse(5, 5))

# temp = 10 	 # global-scope variable
#
# def func():
#       global temp
#       temp = 20   # local-scope variable
#       print(temp)
#
# print(temp) 	 # output => 10
# func() 		 # output => 20
# print(temp) 	 # output => 20
#
# str = "abir"
#
# def stringCount(str):
#       count = 0
#       str = len(str)
#
#       for i in range(str):
#             if i in count:
#                   count += 1
#       return count
# print(stringCount(str))

def number(n):
      length = len(n)
      for i in range(length):
            x = n[i]
      return x
print(number(10))