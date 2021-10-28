num = [4, 5, 7, 8, 2, 24]

second = sorted(num)
print(second[-2])

def maxNum(num):
    max = num[0]
    secondMax = num[0]
    third = num[0]
    for i in range(len(num)):
        if num[i] > max:
            max = num[i]
    for i in range(len(num)):
        if num[i] > secondMax and num[i] != max:
            secondMax = num[i]
    for i in range(len(num)):
        if num[i] > third and num[i] != secondMax and num[i] != max:
            third = num[i]
    return third
print("3rd number", maxNum(num))

def minNum(num):
    min = num[0]

    for i in range(len(num)):
        if num[i] < min:
            min = num[i]
    return min
print("Min number", minNum(num))

def maxIndex(num):
    maxIndex = 0
    maxNum = 0
    second = 0

    for index, number in enumerate(num):
        if number > maxNum:
            maxIndex = index
            maxNum = number
    for index, number in enumerate(num):
        if number > second and number != maxNum:
            second = number
    return "This is 2nd index {} with 2nd value {}".format(maxIndex -1, second)
print(maxIndex(num))
# Dict
# groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}
#
# def maxNumber(num):
#     max = {}
#
#     for current in num.values():
#         if current > max:
#             max = current
#
#     return str(max)
# print(maxNumber(groceries))