'''
Class attributes are specific to the class and not an instance of the class
--> think public and private
'''
class Person:
    number_of_people = 0; #class attribute (no self)
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod #not specific to an instance - acts on the class and not to the instance
    def ret_number_of_people(cls):  #cls references the class only
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1;

p1 = Person("Tim")
print(Person.number_of_people)
p2 = Person("Jim")
print(Person.number_of_people)  #use instance
print(Person.ret_number_of_people()) #use class method