
"""
Decorators: I can add or modify the extra features from exciting function
To wrap another function in order to extend the behavior of the wrapped function,
without permanently modifying it.
"""

def div(a, b):
    print(a/b)

def deco_Div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner

div_1 = deco_Div(div)

div(2, 4)