#    file           class
from Student import Student
from ClubsStudent import ClubsStudent

#object
stnt1 = Student("Jim", "Business", 3.6)
stnt2 = Student("Pam", "Art", 2.5)
club_std1 = ClubsStudent("Matt", "Engineering", 3.3)

print(stnt1.name)
print(stnt2.gpa)

stnt1.do_homework()
club_std1.do_homework()

stnt1.make_excuse()
club_std1.make_excuse()
