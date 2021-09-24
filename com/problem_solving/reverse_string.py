def reverse_string(input_string):
    result = ''
    for x in input_string:
        if x not in result:
            result = x + result
    return result

print(reverse_string("abir"))


theList = [5, 7, 9]
def reverseInt(num):
    res = []
    size = len(num)

    for i in range(size):
        size -= 1
        res.append()

    return res
print(reverseInt(str(theList)))

x = theList[::-1]
print(x)