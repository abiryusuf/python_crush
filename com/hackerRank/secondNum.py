"""
Given list is [2,4,6,6,5. The maximum score is 6 , second maximum is 5 .
Hence, we print 5 as the runner-up score.
"""

# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
# print(sorted(list(set(arr)))[-2])

# def maxNum(num):
#     if len(num) == 0:
#         return 0
#     current_num = [0]
#     max_num = [0]
#
#     for i in num[1:]:
#         current_num = max(current_num + i, i)
#         max_num = max(current_num, max_num)
#     return max_num
# x = [6, 8, 7, -2, 10]
# print(maxNum([x]))

def total(num):
    sum = 0
    for i in num:
        sum += num[i]
    return round(sum, 2)
groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(total(groceries))

def maxNum(num):
    length = len(num)
    max = num[0]
    secondLargest = num[0]

    for i in num:
        # current = num[i]
        if i > max:
            max = i
    for i in num:
        if i > secondLargest and i != max:
            secondLargest = i
    return secondLargest
print(maxNum([5, 7, 8]))

