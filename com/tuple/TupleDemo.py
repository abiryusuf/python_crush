# Tuples are used to store multiple items in single variable
# List is changeable but tuple is immutable( can not change)

result = (1, 23, 20)
hours, mintues, seconds = result

print(hours, mintues, seconds)


def file_size(file_info):
    name, type, size = file_info
    return ("{:.2f}").format(size / 1024)


print(file_size(('Class Assignment', 'docx', 17875)))

# The formatting expression {:.2f} means that you’d format this as a float number,
# with two digits after the decimal dot.
# The colon acts as a separator from the field name, if you had specified one

