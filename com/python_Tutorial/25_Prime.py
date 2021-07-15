
num = 13

for i in range(2, num):
    if num % i == 0:
        print("NOT PRIME")
        break
else:
    print("Prime number")

x = int(input("Enter Number: "))
def primeNum(num):
    for i in range(2, num):
        if num % i == 0:
            return "Not Prime Number"
        else:
            return "Prime Number"
print(primeNum(x))