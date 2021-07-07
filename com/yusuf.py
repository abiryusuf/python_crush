
def duplicateString(str):

    uniue = []
    seen = set()

    for i in str:
        if i not in seen:
            uniue.append(i)
            seen.add(i)
    return uniue
print(duplicateString("ABBIRIRI"))
