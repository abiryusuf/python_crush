def fun(str):
    res = ""
    s = str.split()
    for i in s:
       res = i + res
    return res

print(fun("welcome to"))

for i, val in enumerate(fun("welcome to abir")):
    print(i, val)