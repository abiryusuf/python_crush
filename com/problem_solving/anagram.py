
# def anagram(str1, str2):
#     word = sorted(str1)
#     word1 = sorted(str2)
#     if word == word1:
#         return True
#     else:
#         return False
#
# print(anagram("abcd", "cdab"))

# 2nd ways anagrams
def anagreamsSecound(s1, s2):
    # remove space and lower case
    String1 = s1.replace(" ", "").lower()
    r = sorted(String1)
    String2 = s2.replace(" ", "").lower()
    y = sorted(String2)
    if r == y:
        return True
    else:
        return False
print(anagreamsSecound("abir", "yusuf"))

# 3rd anagram
def thirdAnagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # check if same number of letters
    if len(s1) != len(s2):
        return False
    # count frequency of each letter
    count = {}

    for letter in s1:  # for ever letter in first string
        if letter in count:     # if letter in already in dictionary then
            count[letter] += 1  # add 1 to that letter key
        else:
            count[letter] = 1
# do reverse for 2nd string
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:     # every letter has to be 0 before count
        if count[k] == 0:
            return True
    return False
# str1 = input("String1")
# str2 = input("String2")

# sorted_str1 = sorted(str1)
# sorted_str2 = sorted(str2)

names = ["abir", "yusuf", "mim"]
print("Here is the original list")
print(names)

print("\nHere is the sorted list")
print(sorted(names))

print("\nHere is the original list again")
print(names)

print(sorted(names, reverse=True))

x = thirdAnagram("i am abir", "I am abir")
print(x)


