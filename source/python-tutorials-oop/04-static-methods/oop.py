class Maths:

    @staticmethod #they do something but dont change anything
    def add5(x):
        return x+5

    @staticmethod
    def pr():
        print("run")

print(Maths.add5(2))
Maths.pr()