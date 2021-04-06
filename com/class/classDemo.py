

class MyClass:
    x = 8

ab = MyClass()
print(ab.x)

class Person:
  def __init__(x, name, age):
    x.name = name
    x.age = age

  def myfunc(y):
    print("Hello my name is " + y.name)

p1 = Person("Abir", 30)
p1.age = 23
print("My name is {} and age is {}".format(p1.name, p1.age))
p1.myfunc()

