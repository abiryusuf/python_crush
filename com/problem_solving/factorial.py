def factorial(num):
    count = 1
    for value in range(1, num + 1):
        count = count * value
    return count
print(factorial(5))

for x in range(5):
    print("\n Number: " + str(x))
