# given a list, return a boolean indicates if match item is in the list

def matcher(lst, match):
    for item in lst:
        if item == match:
            return True
    return False
items = [1, 3, 5, 6, 7]
print(matcher(items, 10))
