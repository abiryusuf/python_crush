
def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)
fib(-3)
    # if n == 1:
    #     return 1
    # else:
    #     return fib(n - 1) + fib(n - 2)
# print(fib(10))