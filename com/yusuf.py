# #
# # def duplicateString(str):
# #
# #     uniue = []
# #     seen = set()
# #
# #     for i in str:
# #         if i not in seen:
# #             uniue.append(i)
# #             seen.add(i)
# #     return uniue
# # print(duplicateString("ABBIRIRI"))
# #
# # x = [2, 4, 6, 7]
# #
# # print(x.copy())
#
# n = [1, 3, 5, 7]
#
#
# # def maxNum(num):
# #     length = len(num)
# #     max = 0
# #
# #     for i in range(length):
# #         current = num[i]
# #         if current > max:
# #             max = current
# #     return max
# # print(maxNum(n))
#
# # def str_1(num):
# #    num = num.reverse()
# #    length = len(num)
# #    res = []
# #    for i in range(length):
# #        res = num[i]
# #        return res
# # print(n)
#
# theList = [1, 3, 6]
# reversed_l = theList.reverse()
# print(list(theList))
#
# # test_str = ‘gfg*is*best’, delim = “*”
# # Output : {0: ‘gfg’, 1: ‘is’, 2: ‘best’}
#
#
# def func(num):
#     a = num
#     b = 1
#     e = 0
#     while (a - b > e):
#         a = (a + b)/2
#         b = num/a
#     return a
# def find(N):
#     num = 1 + 8*N
#     maxNum = (-1 + func(num)) / 2
#     return round(maxNum)
# N = 7
# print(find(N))
# theList = [2, 5, 7, 8]
#
# def secondHightst(num):
#     size = len(num)
#     max = {}
#
#     for i in range(1, size):
#         current = num[i]
#         if current > max:
#             max = current
#     return max - 1
# print(secondHightst(theList))

