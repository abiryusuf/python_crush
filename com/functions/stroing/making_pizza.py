import pizza
from pizza import *
# if function is conflict or long name, I can use a short, unique alias
from pizza import make_pizza as x
x(45, "abr")
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'av', 'cd')

