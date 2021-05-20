def factorial(n):
    sum = 1

    for i in range(1, n):
        sum += sum * i
    return sum
print(factorial(5))


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
print(fact(4))
