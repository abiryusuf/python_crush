# the loop is execute the set of statements

colors = ['red', 'black', 'white', 'green']

# for color in colors:
#     print("\nMy favorite color " + color.title())

# loop through the a string
# name = 'abir yusuf'
# for names in name:
#     print(names)


# With break statement we can stop loop before it has looped through the all item
for color in colors:
    if color == 'white':
        break
    print("Break " + str(color))
