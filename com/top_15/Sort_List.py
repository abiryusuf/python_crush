"""
Write a sort function to sort the elements in list

"""
thisList = [4, 6, 2, 6]
thisList.sort(reverse=True)
print(thisList)

"""
write a sorting list function without using the list.sort function 
"""

def SortFunction(data):
    new_list = []
    while data:
        minimum = data[0]
        for i in data:
            if i > minimum:
                minimum = i
        new_list.append(minimum)
        data.remove(minimum)
    return new_list
print(SortFunction(thisList))