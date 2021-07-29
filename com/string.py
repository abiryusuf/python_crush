# # count letter from the sentence
#
# info = "I am Abir am"
#
# def count_letter(str):
#     res = {}
#     str = str.replace(" ", "").lower()
#
#     for i in str:
#         if i in res:
#             res[i] += 1
#         else:
#             res[i] = 1
#     return res
# print("count letter", count_letter(info))
#
# # count letter
# def count_word(str):
#     res = {}
#     str = str.split(" ")
#
#     for word in str:
#         if word in res:
#             res[word] += 1
#         else:
#             res[word] = 1
#     return res
# print("count word", count_word(info))
#
# # get word
#
# def get_word(sentence, num):
#     if num > 0:
#         word = sentence.split()
#         if num <= len(word):
#             return word[num - 1]
#         else:
#             return "don't find in the sentence"
#
# print(get_word(info, 3))
#
# def count_vowel(str):
#
#     count = 0
#     for i in str:
#         if i in "aeiou":
#             count += 1
#     return count
# print(count_vowel(info))

# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# def func(num):
#
#     sum = 0
#
#     for i in num:
#         if i <= 6:
#             sum += i
#     return sum
# print(func([1, 2, 3, 4, 5, 6, 7, 8]))

