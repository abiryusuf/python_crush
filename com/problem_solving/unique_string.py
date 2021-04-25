def unique_string(string):
    string.replace(" ", "")
    char = set()

    for letter in string:
        if letter in char:
            return False
        else:
            char.add(letter)
    return True

def unique(string):
    str = string.replace(" ", "")
    return len(set(str)) == len(str)

print(unique('a b c d d'))
print(unique_string(" a b c d d"))
