# count letter from the sentence

info = "I am Abir am"

def count_letter(str):
    res = {}
    str = str.replace(" ", "").lower()

    for i in str:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res
print("count letter", count_letter(info))

# count letter
def count_word(str):
    res = {}
    str = str.split(" ")

    for word in str:
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
    return res
print("count word", count_word(info))

# get word

def get_word(sentence, num):
    if num > 0:
        word = sentence.split()
        if num <= len(word):
            return word[num - 1]
        else:
            return "don't find in the sentence"

print(get_word(info, 3))

def count_vowel(str):
    size = len(str)
    count = ""
    for i in range(1, size):




