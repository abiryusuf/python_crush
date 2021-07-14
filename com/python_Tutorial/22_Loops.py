# execute the set of statements as long as condition is true

# i = 1
#
# while i < 6:
#     print("Hello", i)
#     if i == 3:
#         continue
#     i += 1

# Break: jum out of the loop or exit the loop
# av = 5
# x = int(input("How many candies you want ?"))
# i = 1
# while i <= x:
#     if i > av:
#         print("out of stock ")
#         break
#     print("Candy")
#     i += 1
# print("Bye")

# Continue: it will stop the current iteration of the loop and continue the next
# for i in range(1, 10):
#     if i % 3 == 0 or i % 5 == 0:
#         continue
#     print(i)


# Loop can not be empty but sometimes doesn't need loop with content
# So, use the pass statement to avoid the error
for i in range(1, 20):
    if i % 2 != 0:
        pass
    else:
        print(i)