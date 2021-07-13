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

    for i in range(1, size):
        if i not in res:
            res = i + res
    return res
print(reverseInt(theList))