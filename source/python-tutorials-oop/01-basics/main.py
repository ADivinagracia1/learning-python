from Student import Student
from Course import Course

s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 20, 75)
s3 = Student("Jill", 19, 65)

c1 = Course("Calculus", 2)
c1.add_student(s1)
c1.add_student(s2)
print(c1.add_student(s3))
print(c1.get_average_grade())