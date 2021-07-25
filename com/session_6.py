"""
Python program to split the string and convert it to dictionary
"""

test_str = 'gfg*is*best*for*geeks'
x = test_str.split("*")
res = {}

for i, value in enumerate(x):
    res[i] = value
print(str(res))

