theList = [3, 3, 5, 6, 6, 6, 7, 7]

print(set([x for x in theList if theList.count(x) > 1]))

def duplicate_value(num):
    seen = set()
    unique = []

    for value in num:
        if value not in seen:
            unique.append(value)
            seen.add(value)
    return unique

print(duplicate_value([1, 2, 2, 4, 3, 6, 6, 6]))

info = "I am abir"

print(len(info.split()))

def countWord(str):
    str = str.replace(" ", "").lower()
    res = ""
    for i in str:
        if i not in res:
            res += 1
        return res
print(countWord(info))

