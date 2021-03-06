# Use a dictionary to count the frequency of letters in the input string. Only letters should be counted, not blank spaces, numbers, or punctuation.
# Upper case should be considered the same as lower case. For example, count_letters("This is a sentence.")
# should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

def count_letter(text):
    result = {}

    for letter in text:
        if letter not in result:
            result[letter.lower()] = 1
        else:
            result[letter.lower()] += 1
    return result
print(count_letter("This is the sentence"))
