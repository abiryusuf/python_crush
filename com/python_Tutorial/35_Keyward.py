
"""
The special syntax *args in function definition in python is used to pass a variable
number of arguments to a function. It is used to pass non-key worded, variable-length argument list
"""
def info(*args):
    for arg in args:
        print(arg, end=' ')
info('I', 'am', 'abir')

"""
The special syntax **kwargs in function definitions in python is used to pass a keyworded, 
variable-length list. 
"""
def info_1(**kwargs):
    for i, j in kwargs.items():
        print("\n", "%s == %s" % (i, j))
info_1(first = 'I', mid = 'Am', last = 'Avir')