# def duplicate(num):
#     dup = []
#     seen = set()
#
#     for value in num:
#         if value not in seen:
#             dup.append(value)
#             seen.add(value)
#     return dup
#
#
# print(duplicate([1, 1, 2, 2, 2, 5, 6, 6]))
#
# # list comprehensions
# def list_duplicate(n):
#     seen = set()
#     uniq = [x for x in n if x not in seen and not seen.add(x)]
#     return uniq
# print(list_duplicate([1, 2, 3, 3, 4, 4]))
#
# def sum(num):
#     res = 0
#
#     for x in range(1, num + 1):
#         res += x
#     return res
#
#
# print(sum(5))
#
#
# def factorial(n):
#     count = 1
#
#     for x in range(1, n + 1):
#         count = count * x
#     return count
#
#
# x = factorial(5)
#
# print("Factorial " + str(x))

#
# def total(n):
#     sum = 0
#     for value in n:
#         sum += n[value]
#     return round(sum, 2)
# groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}
# number = [1, 2, 4, 5]
# x = total(groceries)
# print("Total Price " + str(x))
#
# number = [1, 2, 4, 5]
#
# def sumNum(n):
#     sum = 0
#
#     for x in n:
#         sum += x
#     return sum
# print("Total {}".format(sumNum(number)))

# def palindrome(n):
#     str1 = ""
#     str2 = ""
#     for x in n:
#         if x != "":
#             str1 += x
#             str2 = x + str2
#     if str1 == str2:
#         return True
#     return False
# print(palindrome("madam"))

# def non_repeating(string):
#     str = string.replace(" ", "").lower()
#     count = {}
#     for x in str:
#         if x in count:
#             count[x] += 1
#         else:
#             count[x] = 1
#     for x in str:
#         if count[x] == 1:
#             return x
#     return None
#
# print(non_repeating("I am abir"))
#
# def count_letter(text):
#     text = text.replace(" ", "").lower()
#     count = {}
#
#     for letter in text:
#         if letter in count:
#             count[letter] += 1
#         else:
#             count[letter] = 1
#     return count
# print(count_letter("abir yusuf"))

def anagram(s1, s2):
    count = {}

    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    # reverse
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] == 0:
            return True
    return False
print(anagram("abir", "bira"))

def palindrome(s):
    new_string = ""
    old_string = ""
    res = ""

    for letter in s:
        if letter != res:
            new_string += letter
            old_string = letter + old_string
    # print("new string {} - old_string {}".format(new_string, old_string))
    # if new_string == old_string:
    #         return True
    # return False
print(palindrome("abir"))

