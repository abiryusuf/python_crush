theList = [12, 16, 18, 21, 23]

for num in theList:
    if num % 5 == 0:
        print(num)
        break
else:
    print("Not Found")
