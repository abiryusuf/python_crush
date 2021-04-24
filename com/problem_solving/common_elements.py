

def common_element(a, b):
    num1 = 0
    num2 = 0

    result = []

    while num1 < len(a) and num2 < len(b):
        if a[num1] == b[num2]:
            result.append(a[num1])
            num1 += 1
            num2 += 1
        elif a[num1] > b[num2]:
            num2 += 1
        else:
            num1 += 1
    return result

print((common_element([1,3,4,5], [1,2,3,4])))