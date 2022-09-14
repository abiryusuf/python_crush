sentence = "I am abir"

# for letter in sentence:
#     print(letter)

words = sentence.split()
print(len(words))

for word in words:
    print(word)

def get_word(sentence, n):
    if n > 0:
        words = sentence.split()
        print(words)
        if n <= len(words):
            return (words[n-2])
    return("")
print(get_word("This is a lesson about lists", 4))

name = "My name is abir yusuf"
name_1 = name.split()
print(name_1[4 - 1])

def word(name, n):
    name_2 = name.split()
    if n <= len(name_2):
        return name_2[n - 1]
    return ''
print(word(name, 2))