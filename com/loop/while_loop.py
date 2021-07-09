# execute the set of statements as long as condition is true



# x = "abir"
# y = ""
# z = ""
# for i in x:
#     y = i + y
#     z = z + i
#     if y == z:
#         print("It is plaindrome")
#     else:
#         print("It is not")
x = input("Enter String: ")
def palindrome(str):
    str = str.lower()
    new = ""
    reverse = ""
    for i in str:
        if i != "":
            new = new + i
            reverse = i + reverse
    if new == reverse:
        return "It is palindrome"
    return "It is not"
print(palindrome(x))

