name = ['yusuf',"abir", 'mim', 'madiha']
print(sorted(name))

# def anagram_first(str1, str2):
#     x = str1.lower()
#     y = str2.lower()
#     if x == y:
#         return True
#     return False
# z = anagram_first("abir", 'abir')
# print(z)

# def anagram(str1, str2):
#     x = str1.replace(" ", "").lower()
#     y = str2.replace(" ", "").lower()
#     string1 = sorted(x)
#     string2 = sorted(y)
#     if string1 == string2:
#         return True
#     return False
# print(anagram("public relations", "crap built on lies"))

def anagramFinal(str1, str2):
    x = str1.replace(" ", "").lower()
    y = str2.replace(" ", "").lower()

    if len(x) == len(y):
        return True

    count = {}

    for letter in str1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    for letter in str2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    for k in count:
        if count[k] == 0:
            return True
        return False

print(anagramFinal("public relations yusuf", "crap built on lies abir"))
print(anagramFinal("abir", "yusuf"))


