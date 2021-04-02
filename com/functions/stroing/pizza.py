# one advantage of function is the way they separate blocks of code from your main program.
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
          '-inch pizza with the following topping: ')
    for topping in toppings:
        print("- " + topping)
