# You are given a string and your task is to swap cases. In other words, convert
# all lowercase letters to uppercase letters and vice versa.
s = 'AbiR yusuf'
def swap_case(s):
    x = ""
    for i in s:
        if i.isupper():
            y = i.lower()
        else:
            y = i.upper()
        x +="".join(y)
    return x
print(swap_case(s))