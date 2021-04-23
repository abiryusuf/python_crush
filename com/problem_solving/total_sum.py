
# Given an array of integers (positive and negative ) find the largest continuous sum
def largestNum(arr):
    if len(arr) == 0:
        return 0
    max_sum = arr[0]
    current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum
print(largestNum([3, 7, 8, -8, 10]))