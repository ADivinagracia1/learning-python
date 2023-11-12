#Generalization Class
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old") #F String POGGERS

    def speak(self):
        print("...")

#inheritance
class Cat(Pet): #===================================================================
    def __init__(self, name, age, color):
        super().__init__(name, age) #reference the Super Class, Pet
        self.color = color

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old, and I am {self.color}")

    def speak(self):
        print("Meow")

class Dog(Pet): #===================================================================
    def speak(self):
        print("Woof")

class Fish(Pet): #==================================================================
    pass

# ====================================== MAIN ======================================
p1 = Pet("Tim", 3)
p1.show()
p1.speak()

c1 = Cat("Jack", 2, "Orange")
c1.show()
c1.speak()

d1 = Dog("Alfred", 9)
d1.speak()

f1 = Fish("Bubbles", 7)
f1.speak()