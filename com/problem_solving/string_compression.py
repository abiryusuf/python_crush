def compress(s):
    r = ''
    l = len(s)

    if l == 0:
        return ""
    if l == 1:
        return s + "1"
    # Initialize values
    last = s[0]
    count = 1
    i = 1

    while i < l:
        # Check to see if it is the same letter
        if s[i] == s[i-1]:
            # Add a count if same as previous
            count += 1
        else:
            # otherwise store the previous data
            r = r + s[i - 1] + str(count)
            count = 1
        # add to index count to terminate while loop
        i += 1
    # put everything back into run
    r = r + s[i - 1] + str(count)
    return r
print(compress("aabb"))