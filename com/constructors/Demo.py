class Demo:

    f_name = "".upper()
    l_name = "".upper()

    def __init__(self, firstName, lastName):
        self.f_name = firstName
        self.l_name = lastName

    def display(self):
        print("First Name: " + self.f_name)
        print("Last Name: " + self.l_name)

obj = Demo("abir", "yusuf")
obj.display()