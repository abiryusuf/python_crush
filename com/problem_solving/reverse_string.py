def reverse_string(input_string):
    result = ''
    for x in input_string:
        if x not in result:
            result = x + result
    return result

print(reverse_string("abir"))
