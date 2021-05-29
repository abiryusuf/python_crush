# given a list, return a boolean indicates if match item is in the list

def matcher(lst, match):
    for item in lst:
        if item == match:
            return True
    return False
items = [1, 3, 5, 6, 7]
print(matcher(items, 10))

x = 1 in items
print(x)


def match1(value, match):
    for i in value:
        if i == match:
            return True
    return False
print(match1(items, 5))

def liner(item, taget)