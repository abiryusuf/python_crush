def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""
    for x in input_string:
        if x != "":
            new_string = new_string + x
            reverse_string = x + reverse_string
    if new_string == reverse_string:
        return True
    return False
print(is_palindrome("madam"))



