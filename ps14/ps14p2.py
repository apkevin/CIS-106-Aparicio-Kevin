'''
2.	Create a student class. This class should consist of student 
first name, student last name, district code (I or O) and enrolled credits. 
Create a method to compute tuition owed. 
Tuition owed should be enrolled credits times $250.00 per credit hour for in district students (district code of I)
and or times $500.00 per credit hour for out of district students (district code of anything other than I). 
Test the class by instantiating the object and adding data. 
'''

class Student:

    def __init__(self, first, last, district, credits):
        self.first = first
        self.last = last
        self.district = district
        self.credits = credits

    def tuition(self):
        if self.district == "I":
            cost = float(self.credits) * 250.00
        elif self.district == "O":
            cost = float(self.credits) * 500.00
        return cost
    
stu1 = Student("Kevin", "Ap", "I", 12)
stu2 = Student("Max", "Mawwell", "O", 12)

print(stu1.first)
print(stu1.last)
print(stu1.district)
print(stu1.credits)

print(stu2.first)
print(stu2.last)
print(stu2.district)
print(stu2.credits)

print(stu1.tuition())
print(stu2.tuition())