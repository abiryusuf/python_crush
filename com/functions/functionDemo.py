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

# Returning a dictionary
# benefits in function using dictionary
# I can easily extend this function to accept optional values like
# a middle name, an age, an occupation, or
# any other information you want to store about a person.

def build_person(f_name, l_name, age=''):
    """Return a dictionary of information about a person"""
    person = {
        'first': f_name.title(),
        'last': l_name.title()
    }
    if age:
        person['age'] = age
    return person
u = build_person('abir', 'yusuf')
print(u)
z = build_person('mim', 'monira', 4)
print(z)


def get_full_name(first_name, last_name):
    fullName = first_name + " " + last_name
    return fullName.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First Name: ")
    if f_name == 'q':
        break

    l_name = input("Last Name: ")
    if l_name == 'q':
        break


x = get_full_name(f_name, l_name)
print("\nHello, " + x)