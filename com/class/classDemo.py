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
p1.age = 23
print("My name is {} and age is {}".format(p1.name, p1.age))
p1.myfunc()


class Person2:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname

    def fullName(self):
        print(self.firstName, self.lastName)


y = Person2('yusuf', 'abir')
y.fullName()


class Students(Person2):
    pass


t = Students("Mim", 'Madiha')
t.fullName();
