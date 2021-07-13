
"""
Write a program to print prime number between 100 and 200
"""
for num in range(100, 200):
    # if all(num % i != 0 for i in range(2, num)):
    #     print(num)
    if num % 2 == 0:
        print("Prime Number: " + str(num))

prime = int(input("Enter the number: "))
def primeNum(num):

    if num % 2 == 0:
        return "It is prime"
    else:
        return "It is not prime number"

print(primeNum(prime))