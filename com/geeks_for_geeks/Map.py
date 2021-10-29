"""
Python's map() is a built-in function that allows you to process and transform
all the items in an iterable without using an explicit for loop, a technique
commonly known as mapping. map() is useful when you need to apply
 a transformation function to each item in an iterable and transform
 them into a new iterable.

 MAP vs FILTER
Map takes all objects in a list and allows you to apply a function to it.
Filter takes all objects in a list and runs that through a function
to create a new list with all objects that return True in that function.

filter - map - reduce
from Data: filter the data which one i don't need, map the data what i need
to change or updated data and reduce the data

"""
from functools import reduce
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

def add_all(a, b):
    return a + b

nums = [2, 3, 4, 5, 6, 8, 9, 10]
evens = list(filter(lambda n: n % 2 == 0, nums))

maps = list(map(lambda n: n * 2, evens))

sum = reduce(lambda a, b: a + b, maps)


print(evens)
print(maps)
print(sum)

