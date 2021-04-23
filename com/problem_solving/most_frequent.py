"""
Given an array what is the most frequently occuring element
"""

def most_frequent(list):
    count = {}
    max_count = 0
    max_item = None

    for x in list:
        if x not in count:
            count[x] = 1
        else:
            count[x] += 1

        if count[x] > max_count:
            max_count = count[x]
            max_item = x

    return max_item

print(most_frequent([1,1,3,5,6,7,7,7,]))