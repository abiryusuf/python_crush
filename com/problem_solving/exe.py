sen = "I am abir yusuf"

def count_letter(text):
    res = {}

    for letter in text:
        if letter in res:
            res[letter.lower()] += 1
        else:
            res[letter.lower()] = 1
    return res

print(count_letter(sen))

def reverse(str):

    res = ""
    for x in str:
        if x not in res:
            res = x + res
    return res
print(reverse("abir yusuf"))
