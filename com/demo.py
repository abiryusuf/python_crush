text = "abirr"
def unique(str):
    seen = set()
    for x in str:
        if x in seen:
            return False
        else:
            seen.add(x)
    return True
print(unique(text))

number = [1,2,3,3,5,6,6]
def duplicate(num):
    seen = set()

    dup = []

    for x in num:
        if x not in seen:
            dup.append(x)
            seen.add(x)
    return dup
print(duplicate(number))

def num(n):
    sum = 0

    for x in range(1, n + 1):
        sum += x
    return sum
print(num(5))

def sum(n):
    total = 0
    for value in n:
        total += value
    return total
print(sum(number))



