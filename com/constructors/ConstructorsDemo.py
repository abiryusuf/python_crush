"""
Constructors are used for instantiating an object
After creating an object of class that allows to access the value or data of the
class

"""
class Con:
    # def __init__(self):
    #     self.name = "abir".upper()
    f_name = 'abir'
    l_name = "yusuf"

    def firstName(self):
        print(self.f_name, self.l_name)

    first = 0
    second = 0
    third = 0
    answer = 0

    def __init__(self, f, s, t):
        self.first = f
        self.second = s
        self.third = t

    def display(self):
        print("First Number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Third Number = " + str(self.third))
        print("Total = " + str(self.answer))

    def cal(self):
        self.answer = self.first + self.second - self.third

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def dis(self):
        print("Name " + str(self.name))


obj = Con(2, 5, 3)
obj.firstName()
obj.cal()
obj.display()
obj.dis()


