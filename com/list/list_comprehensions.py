# List comprehensions allow you to create a new list from a sequence
# or a range in a single line.
multiple = []

for num in range(1, 10):
    multiple.append(num * 2)

print(multiple)

# list comprehensions
multiple = [x*2 for x in range(1, 10)]
print(multiple)


# conditions
add = [y + 2 for y in range(1, 10 + 1) if y % 2 == 0]
print(add)

# how to find length or word from list
languages = ["Java", "Perl", "Python", "C++"]
def length_list(num):
    lengths = [len(x) for x in num]
    return "word length " + str(lengths)
print(length_list(languages))

for language in languages:
    print(len(language))

for index, language in enumerate(languages):
    print("{} - {}".format(index + 1, len(language)))




