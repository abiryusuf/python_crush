'''

Array pair sum
Given an integer array, output all the unique paris that sum up to a
specific value k
e.g pair_sum([1,3,2,2], 4)
return 2 pairs :
(1,3)
(2,3)

'''
def pair_sum(array, k):
    if len(array) < 2:
        return print("Too small")
    seen = set()
    output = set()

    for num in array:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max((num, target))))
    print("\n".join(map(str, list(output))))

pair_sum([1, 3, 2, 2, 5, -1], 4)

arr = [2, 4, 6, 8]
x = 2
for i in arr:
    tar = x - i
    print(tar)
