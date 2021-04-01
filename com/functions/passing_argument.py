
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

