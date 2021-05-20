import sys
sys.setrecursionlimit(100)

print(sys.getrecursionlimit())
def myFun():
    count = 0
    count += 1
    print("Hlw", count)
    myFun()

myFun()

# def printInc(n):
#     if n > 0:
#         printInc(n - 1)
#         print(n)
# printInc(4)