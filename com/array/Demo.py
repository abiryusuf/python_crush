import array as arr

my_list = [2, 3, 5, 7, 11]

squared_list = [x**2 for x in my_list]    # list comprehension
# output => [4 , 9 , 25 , 49 , 121]
print(squared_list)
squared_dict = {x:x**2 for x in my_list}    # dict comprehension
# output => {11: 121, 2: 4 , 3: 9 , 5: 25 , 7: 49}

print(squared_dict)

my_arr = arr.array('i', [1, 3, 5])
x = my_arr[::-1]

print(x)

def reverseNum(n):
    rev = 0
    while n > 0:
        a = n % 10
        rev = rev * 10 + a
        n = n // 10
    return rev
print(reverseNum(4562))