"""
Bubble Sort: Rearranges the value by iterating over the list multiple times, causing
larger values to bubble to the top or end of the list.

Main reasons is find the large value from end of the list
Bubble sort needs two loops
"""
arr = [2, 5, 1, 3]
x = sorted(arr)
n = len(x)

for i in range(1, n - 1):
    print(i)

evenOdd = int(input("Enter the number: "))
def EvenOdd(num):

    if num % 2 == 0:
        return "Even"
    else:
        return "odd"
print(EvenOdd(evenOdd))