arr = [1, 2, 4, 6]

def minMax(arr):
    count = 0
    minnum = 9999999
    maxnum = 0

    for i in range(len(arr)):
        count += arr[i]
        minnum = min(minnum, arr[i])
        maxnum = max(maxnum, arr[i])
    return count - minnum, count - maxnum
print(minMax(arr))
