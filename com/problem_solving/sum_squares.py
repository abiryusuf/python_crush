def sum_square(x):
    sum = 0
    for n in range(x):
        sum += n + n
    return sum
print(sum_square(10))

values = [5, 6, 78, 9, 23]

def sumNum(num):
    sum = 0
    for value in num:
        sum += value
    return sum
print("Total: {}".format(sumNum(values)))
print('Total: ' + str(sumNum(values)))

animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
char = 0

for animal in animals:
    char += len(animal)
    print("Total character: {}, Average length {}".format(char, char/len(animal)))


Numbers = [90, 88, 95, 78]
sum1 = 0
length = 0
for number in Numbers:
    sum1 += number
    length += 1
print("Total: " + str(sum1) + " - Average " + str(sum1/length))


