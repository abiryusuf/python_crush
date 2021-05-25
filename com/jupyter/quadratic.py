# prints paris for every item in list
def func_quad(lst):
    for item_1 in lst:
        for item_2 in lst:
            print(item_1, item_2)
x = [1,3,4,5,6]
func_quad(x)