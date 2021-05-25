def exp1(x, n):
    y = 1
    for i in range(n):
        y *= x
    return y
print(exp1(3, 2))

def exp(x, n):
    if n == 0:
        return 1
    res = exp(x * x, n // 2)
    if n % 2 == 0:
        return res
    else:
        x * res
    return res
print(exp(3, 2))

