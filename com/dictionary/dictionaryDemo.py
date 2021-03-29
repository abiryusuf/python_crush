info = {
    'name': 'abir',
    'age': 32,
    'place': 'NT'
}
print(info)
info['email'] = 'abir.com'

print(info)

file_counts = {"jpg": 10, "text": 14, "csv": 2, "py": 23}
print(file_counts.items())

# for key in file_counts.keys():
#     print(key)

for keys, values in file_counts.items():
    print('THere are {} files with the {}'.format(keys, values))

sentence = 'I am abir'
def count_letter(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result
print(count_letter(sentence))

