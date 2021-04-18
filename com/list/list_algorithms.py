# change the file name
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

new_fileNames = []
for name in filenames:
    if name.endswith(".hpp"):
        name = name.replace("hpp", 'h')
        new_fileNames.append(name)
    else:
        new_fileNames.append(name)
print(new_fileNames)
