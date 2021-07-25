"""
Python program to split the string and convert it to dictionary
"""

test_str = 'gfg*is*best*for*geeks'
x = test_str.split("*")
res = {}

for i, value in enumerate(x):
    res[i] = value
print(str(res))


" Python Program to find largest element in an array "
num = [3, 6, 8, -3, -4]
def largestNum(n):
    size = len(n)

    if len(n) == 0:
        return False
    max = n[0]
    min = n[0]

    for i in range(1, size):
        current = n[i]
        if current < min:
            min = current
    return min
print(largestNum(num))