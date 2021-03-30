def greet_user(userName):
    """"Display a simple+ greeting."""
    print("Hello " + userName.title())

greet_user('Abir')

""""Try it yourself"""
def display_message():
    print("What are you learning about this chapter")
display_message()

def favorite_book(book):
    print("One of my favorite books is " + book.title())
favorite_book("How to influence people")

def add(x, y):
    print("Total: " + str(x + y))

add(3, 5)
# positional argument
# multiple function calls and follow the order argument
def info(first_name, last_name, age):
    print('\nMy first name is: ' + first_name.title())
    print("My last name is: " + last_name.title())
    print("My full name is {} {} and age is {}".format(first_name.title(), last_name.title(), age))

info("abir", 'yusuf', 32)
info("mim", 'monira', 4)

# return value
def name(first_name, last_name):
    fullName = first_name + ' ' + last_name
    return fullName.title()
x = name('abir', 'yusuf')
print(x)

def get_formatted(first, last, middle=''):
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

y = get_formatted('abir', 'yusuf')
print(y)
x = get_formatted('a', 'v', 'c')
print(x)






