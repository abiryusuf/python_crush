def non_repeating(string):
    str = string.replace(' ', '').lower()

    count = {}
    for char in str:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char in str:
        if count[char] == 1:
            return char
    return None
# with key and value
# y = sorted(count.items(), key=lambda x: x[1])
print(non_repeating(" x I am abir"))