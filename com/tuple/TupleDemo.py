# Tuples are used to store multiple items in single variable
# List is changeable but tuple is immutable( can not change)

result = (1, 23, 20)
hours, mintues, seconds = result

print(hours, mintues, seconds)


def file_size(file_info):
    name, type, size = file_info
    return ("{:.2f}").format(size / 1024)


print(file_size(('Class Assignment', 'docx', 17875)))

# The formatting expression {:.2f} means that you’d format this as a float number,
# with two digits after the decimal dot.
# The colon acts as a separator from the field name, if you had specified one

languages = ['Python', 'C', 'C++', 'Java']
for i, language in enumerate(languages):
    print("{} - {}".format(i+1, language))


animals = ["Lion", "Zebra", "Dolphin", "Monkey"]

char = 0

for animal in animals:
    char += len(animal)
    print("Total characters: {}, Average: {}".format(char, char/len(animal)))

def skip_elements(elements):
    ele = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            ele.append("{}".format(element))
    return ele
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))

tuple1 = ((1, 'a'), (4, 'c'), (2, 'd'), (3, "e"))
print(sorted(tuple1))

# now I want to sorted by 2nd items
# use the key function

def secondItems(element):
    # retrieve the 2nd item
    return element[1]
print(sorted(tuple1, key=secondItems))

num = (3, 5, 6, 8)
num.count()
print(num)