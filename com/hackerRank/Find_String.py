"""In this challenge, the user enters a string and a substring.
You have to print the number of times that the substring
occurs in the given string. String traversal will take
place from left to right, not from right to left."""

def count_subString(str, sub_str):
    count = 0
    length = len(sub_str)
    for i in range(len(str)):
        s = str[i:i+length]
        if s == sub_str:
            count += 1
    return count
print(count_subString("abirr", "irr"))