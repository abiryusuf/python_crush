
# passing list
def greet_user(names):
    """"Print a simple greeting to each user name in the list"""
    for name in names:
        msg = 'Hello: ' + name.title()
        print(msg)
username = ["abir", 'yusuf', 'mim']
greet_user(username)

