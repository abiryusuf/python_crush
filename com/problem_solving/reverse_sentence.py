def rev_word(s):
    words = []
    length = len(s)
    spaces = [' ']

    i = 0
    while i < length:
        if s[i] not in spaces:
            start = i
            while i < length and s[i] not in spaces:
                i += 1
            words.append(s[start:i])
            i += 1
     return ''.join(reversed(s))

print(rev_word("I am abir"))


def reverse(s):
    r = " "
    return r.join(reversed(s.split()))
print(reverse("I am abir"))

def rev(s):
    r = s.split()[::-1]
    return r
print(rev('I am abir'))


