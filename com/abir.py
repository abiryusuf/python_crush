# import sys
# from re import Scanner *
#
# from scanner import *
# arr=[]
# def abir():
#     print(sys.argv[0])
#     for i in range(1,len(sys.argv),1):
#         print("   argument",i,"is", sys.argv[i])
#     tokens = readTokens("text.txt")
#     cleanTokens = depunctuateTokens(arr)
#     words = decapitalizeTokens(cleanTokens)
#
# def readTokens(s):
#     s = Scanner("text.txt")
#     token =s.readtoken()
#     while (token != ""):
#         arr.append(token)
#         token=s.readtoken()
#     s.close()
#     return arr
#
# def depunctuateTokens(arr):
#     result=[]
#     for i in range(0,len(arr),1):
#         string=arr[i]
#         cleaned=""
#         punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
#         for i in range(0,len(string),1):
#             if string[i] not in punctuation:
#                 cleaned += string[i]
#         result.append(cleaned)
#     print(result)
#     return result
#
# def decapitalizeTokens(result):
#     if (ord(result) <= ord('Z')):
#         return chr(ord(result) + ord('a') - (ord('A')))
#     else:
#         print
#         return result
# abir()
# list
# my_list = [2, 5, 7, 8]
#
# x = [a * 2 for a in my_list]
# print(x)
#
# y = {i: i * 2 for i in my_list}
# print(y)

def fib(n):
    x = 0
    y = 1
    while x < n:
        yield x
        x, y = y, x + y
x = fib(10)
print(x)

for i in fib(10):
    print(i)

