def sum_square(x):
    sum = 0
    for n in range(x):
        sum += n * n
    return sum
print(sum_square(10))

values = [5, 6, 78, 9, 23]

def sumNum(num):
    sum = 0
    ave = 0
    for value in num:
        sum += value
        ave += 1
    return sum
print('Total ' + str(sumNum(values)))
