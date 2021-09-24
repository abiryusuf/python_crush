"""
Three keywords follow python exception
try: the block lets test a block of code for errors
except: block lets you handle the error
finally: final block will execute code condition true or false
"""

a = 6
b = 0


try:
    print("Open")
    print(a/b)
    # print("Close")
    x = int(input("Enter a number "))
    print(x)
except ZeroDivisionError as e:
    print("Reason ", e)
    # print("I can not divided a Number by Zero", )
    # print("Close")
except ValueError as e:
    print("Reason ", e)
except Exception as e:
    print("Reason ", e)
finally:
    print("Close")

print("Bye")

# if a/b:
#     print("Ture")
# else:
#     print("False")