
# passing list
def greet_user(names):
    """"Print a simple greeting to each user name in the list"""
    for name in names:
        msg = 'Hello: ' + name.title()
        print(msg)
username = ["abir", 'yusuf', 'mim']
greet_user(username)

# Modifying a list in a function
designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# for n in designs:
#     completed_models.append(designs)
#     print(completed_models)
while designs:
    current_designs = designs.pop()
    print("Printing model " + current_designs)
# Simulate creating a 3d print from the design
    completed_models.append(current_designs)

# Display all completed models
print("\nThe following models have been printed")
for completed_model in completed_models:
    print("\t" + completed_model)

# for design in designs:
#     print("Printing model " + design)
