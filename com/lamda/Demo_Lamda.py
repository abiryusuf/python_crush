

def square(a):
    print(a * a)
square(2)

def add(a, b):
    return a + b
res = add(2, 4)
print(res)

# A lambda function is a small anonymous function that means a function doesn't have name
# A lambda function can take any number of arguments, but can only have one expression
square_func = lambda a: a * a
print(square_func(2))

addFun = lambda a, b, c: a + b - c
print(addFun(3, 4, 3))