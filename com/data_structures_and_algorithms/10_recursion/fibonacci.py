
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
for i in range(1, 5):
    print(fib(i))
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     else:
#         for i in range(2, n):
#             c = a + b
#             a = b
#             b = c
#             print(c)
# fib(-3)
#     if n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
# print(fib(10))

#
def func(n):
    x = (n-1) + (n - 2)
    return x
print("func", func(10))



