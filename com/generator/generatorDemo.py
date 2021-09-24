"""
A generator function is defined like a normal function, but whenever
it needs to generate a value, it uses yield keyword instated return

why do we use generator instated of loop or iterator
let say, 1000 values in data, now if i use for loop for getting the data
it will store all values in memory location and it will take space.
I want to fetch data one by one that is main reason to use generator
I want values what i want from data, not all data in memory. that time i need to use
generator. Main reason is memory efficient


"""

def genFun():
    yield 1
    yield 2
    yield 3

x = genFun()
print(x.__next__())

for i in x:
    if i % 2 == 0:
        print(i)
print("1st function")

def sumSquares(n):
    sum = 0
    for num in range(n):
        sum += num * num
    return sum
print(sumSquares(5))

print("2nd function")
def topTen():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1
y = topTen()
for i in y:
    print(i)
print(y)
# one by one
# print(y.__next__())
# print(y.__next__())
# print(y.__next__())
# for i in y:
#     print(i)

# def generator():
#     for i in range(1, 10 - 1):
#         yield i
# x = generator()
# firstNumber = list(x)
# print(firstNumber)
#
# def fibGenerator(limit):
#
#     # Initialize first two fibonacci numbers
#
#     a = 0
#     b = 1
#     # one by one yield next fibonacci numbers
#     while a < limit:
#         yield a
#         a, b = b, a + b
# x = fibGenerator(5)
# for c in fibGenerator(5):
#     print(c)
#

