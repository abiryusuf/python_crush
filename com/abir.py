
fact = int("Enter Number: ")

def factorial(num):
    res = 1

    for i in range(1, num + 1):
        res = res * i
    return res
print(factorial(fact))
# import math as X
#
# print("The factorial of 5 is : ", end="")
# print(X.factorial(5))