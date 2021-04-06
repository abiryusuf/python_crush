

class MyClass:
    x = 8

ab = MyClass()
print(ab.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Abir", 30)

print("My name is {} and age is {}".format(p1.name, p1.age))
p1.myfunc()

