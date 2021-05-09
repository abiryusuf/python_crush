arr = [20, 3, 2, 1, 5, 4]

def sum(num):
    total = 0
    n = len(num)
    for i in num:
        total += i
    return total
print(sum(arr))


# Total with dictionary

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99,
 "bread": 4.59, "coffee": 6.99, "milk": 3.39, "eggs": 2.98,
 "cheese": 5.44}

def total(num):
    sum = 0
    for i in num:
        sum += num[i]
    return round(sum, 2)
print(total(groceries))

def maxNumber(num):
    max = 0
    n = len(num)
    for i in range(0, n):
        current = num[i]
        if current > max:
            max = current
    return max
print(maxNumber(arr))

def factorial(num):
    res = 1

    for i in range(1, num + 1):
        res = res * i
    return res
print(factorial(5))


duplicate = [2, 2, 3, 4, 4, 6, 6]
def duplicateNum(num):
    unique = []
    seen = set()
    for value in num:
        if value not in seen:
            unique.append(value)
            seen.add(value)
    return unique
print(duplicateNum(duplicate))
