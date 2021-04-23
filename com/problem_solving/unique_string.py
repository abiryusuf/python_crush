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
   return len(set(string)) == len(string)

print(unique('a b def'))