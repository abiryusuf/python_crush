
def anagram(str1, str2):
    word = sorted(str1)
    word1 = sorted(str2)
    if word == word1:
        return True
    else:
        return False

print(anagram("abir", "yusuf"))

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

