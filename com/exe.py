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

def anagram(str1, str2):
    string1 = str1.replace(" ", "").lower()
    string2 = str2.replace(" ", "").lower()

    # word1 = sorted(string1)
    # word2 = sorted(string2)
    # if word1 == word2:
    #     return True
    # return False

    if len(string1) == len(string2):
        return True
    count = {}

    for letter in string1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    for letter in string2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] == 0:
            return True
        return False

print(anagram("I am abir", "I am abir"))