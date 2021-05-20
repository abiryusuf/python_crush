# def printRev(n):
#     if n > 0:
#         return n - 1
#
# print(printRev(4))

def factorial(n):
    res = 1
    for i in range(1, n):
        res = res * i
    return res
print(factorial(5))

def sum(n):
    res = 0
    for i in range(0, n):
        res = i * i
    return res
print(sum(4))


def squares(n):
    for i in range(0, n):
        print(i * i)
squares(4)