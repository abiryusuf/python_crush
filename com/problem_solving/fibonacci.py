def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + (n - 2)
for i in range(1, 5):
    print(fib(i))

def fibGenerator(limit):

    # Initialize first two fibonacci numbers

    a = 0
    b = 1
    # one by one yield next fibonacci numbers
    while a < limit:
        yield a
        a, b = b, a + b
x = fibGenerator(5)
for c in fibGenerator(5):
    print(c)

def topTen():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1
y = topTen()

for i in y:
    print(i)


