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

    first = 0
    second = 0
    answer = 0

    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("First Number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))

    def cal(self):
        self.answer = self.first + self.second

    def firstName(self):
        print(self.f_name, self.l_name)

obj = Con(2, 5)
obj.firstName()
obj.cal()
obj.display()


