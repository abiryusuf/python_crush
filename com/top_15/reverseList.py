theList = [3, 5, 7, 8]

#theList.reverse()

#print(theList)

def rev(n):
    return n[::-1]

print(rev(theList))

def reverse(n):
    length = len(n)
    res = []
    for i in range(length):
        length -= 1
        res.append(n[length])
    return res
print(reverse(theList))