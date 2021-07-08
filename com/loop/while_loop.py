# execute the set of statements as long as condition is true



x = "abir"
y = ""
z = ""
for i in x:
    y = i + y
    z = z + i
    if y == z:
        print("It is plaindrome")
    else:
        print("It is not")
