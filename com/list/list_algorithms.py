# change the file name
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
new_fileNames = []
for name in filenames:
    if name.endswith(".hpp"):
        name = name.replace("hpp", 'h')
        new_fileNames.append(name)
    else:
        new_fileNames.append(name)
print(new_fileNames)

# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# 2nd ways
# list comprehensions
new_fileNames = [name.replace('hpp', 'h') if name.endswith('.hpp') else name for name in filenames]
print(new_fileNames)
