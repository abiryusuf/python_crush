# take an input of n and return the sum of the numbers from 0 to n
def sum(n):
    final_sum = 0
    for x in range(n+1):
        final_sum += x
    return final_sum

print(sum(5))

def factorial(num):
    result = 1
    for x in range(1, num + 1):
        result = result * x
    return result
print(factorial(5))