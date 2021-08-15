# the loop is execute the set of statements

colors = ['red', 'black', 'white', 'green']

# for color in colors:
#     print("\nMy favorite color " + color.title())

# loop through the a string
# name = 'abir yusuf'
# for names in name:
#     print(names)

# Break
# With break statement we can stop loop before it has looped through the all item
# for color in colors:
#     if color == 'white':
#         break
#     print("Break " + color)

# continue
# we can stop the the current iteration of the loop and continue the next
# for con in colors:
#     if con == 'white':
#         continue
#     print('\nContinue ' + con)

# range
# It is possible to specify the starting value by adding a parameter
# for num in range(1, 10+2):
#     print(num)
#
# def rang(n):
#     for number in range(1, n + 1):
#         return n[number]
# print((rang([2, 5, 6, 8, 9])))


# for number in range(0, 10):
#     print(number)

# else
# for x in range(1, 10):
#     if x == 4:
#         continue
#     print(x)
# else:
#     print('DONE')

pat = [1, 3, 2, 1, 2, 3, 1, 0, 1, 3]

for p in pat:
    pass
    if p == 0:
        current = p
        break
    elif p % 2 == 0:
        continue
    print(p)    # output => 1 3 1 3 1

print(current)

