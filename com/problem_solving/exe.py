# def plaindrom(str):
#
#     new_string = ""
#     rev_string = ""
#     for x in str:
#         if x not in new_string and rev_string:
#             new_string = new_string + x
#             rev_string = x + rev_string
#     if new_string == rev_string:
#         return True
#     return False
# print(plaindrom("madam"))


def reverseString(str):
    str1 = str.replace(" ", "")
    res = ""
    for x in str1:
        if x not in res:
            res = x + res
    return res

print(reverseString("abir yusuf"))