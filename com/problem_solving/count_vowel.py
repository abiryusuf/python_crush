info = "I am abir"

def countVowel(ste):
    count = 0

    for i in ste.lower():
        if i in "aeiou":
            count += 1
    return count
print(countVowel(info))

count = {i: 0 for i in "aeiou"}
for i in info.lower():
    if i in count:
        count[i] += 1

for j, k in count.items():
    print(j, k)