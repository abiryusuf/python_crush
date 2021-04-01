
# Passing an Arbitrary number of arguments
# if I don't know how many arguments I can use asterisk * in the parameters
def make_pizza(*toppings):
    """"print the list of topping that have been requested"""
    # print(toppings)
    print("\nMaking a pizza with the following topping: ")
    for topping in toppings:
        print("_ " + topping)

make_pizza("chess")
make_pizza("x", 'y', 'c')

# Using arbitrary keyword argument

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user = build_profile('abir', 'yusuf',
                     locationn='NY', country="Bangladesh")
print(user)

# try it
def list_sandwich(*sandwich):
    print("\n The sandwiches orders: ")
    for san in sandwich:
        print("- " + san)
list_sandwich("a")
list_sandwich('chess', 'D')
list_sandwich("a",'v', 'c')

def user_info(fname, lname, **user_detelies):
    profiles = {}
    profiles['first_Name'] = fname
    profiles['last_Name'] = lname
    for k, v in user_detelies.items():
        profiles[k] = v
    return profiles
x = user_info('avir', 'yusuf', county='USA', City='NY')
print(x)

def make_car(manufacture, model, **car_info):
    car = {}
    car['car_name'] = manufacture
    car['car_model'] = model
    for k, v in car_info.items():
        car[k] = v
    return car
y = make_car('Honda', 'Accord', color='Black', tow_package=True)
print(y)


