
def sort(num):
    n = len(num)
    for i in range(n - 1):
        return i

print(sort([4, 3, 5, 8, 6, 7]))

arr = [3, 4, 2, 2, 3, 5, 7, 9, 5]
print(sorted(arr))

def duplicate(num):
    length = len(num)
    # if length > 0:
    #     return True
    n = sorted(num)
    seen = set()
    dup = []
    for x in n:
        if x not in seen:
            dup.append(x)
            seen.add(x)
    return dup
print(duplicate(arr))

