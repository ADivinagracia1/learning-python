class Student:

    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

    def write_test(self):
        print(self.name + " writes a test")

    def do_homework(self):
        print(self.name + " does their homework")

    def make_excuse(self):
        print("I slept in!")