info = {
    'name': 'abir',
    'age': 32,
    'place': 'NT'
}
print(info)
info['email'] = 'abir.com'

print(info)

file_counts = {"jpg": 10, "text": 14, "csv": 2, "py": 23}

for keys, values in file_counts.items():
    print('THere are {} files with the {}'.format(keys, values))
