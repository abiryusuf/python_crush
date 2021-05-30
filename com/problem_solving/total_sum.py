
# Given an array of integers (positive and negative ) find the largest continuous sum
def largestNum(arr):
    if len(arr) == 0:
        return 0
    current_sum = arr[0]
    max_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum
print(largestNum([3, 7, 8, -8, 10]))

# def sum(num):
#     sum = 0
#     for i in range(1, num + 1):
#         sum += i
#     return sum
# print(sum(5))

def add_price(basket):
    total = 0
    for item in basket:
        total += basket[item]
    return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_price(groceries))

for item, price in groceries.items():
    print("Item {} and Price {}".format(item, price))


def maxNumber(num):
    max = [0]

    for i in num:
        current = num[i]
        if current > max:
            max = current

    return str(max)
x = maxNumber([3, 6, 8, -4, 10])
print(str(x))

