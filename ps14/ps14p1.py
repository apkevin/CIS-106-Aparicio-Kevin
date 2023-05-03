# Python Object-Oriented Programming

'''
1.	Watch the video on creating a simple class. Create the class in the video and test it to make sure it works. 
Add a method to the class that accepts a bonus rate for the employee. 
It should then compute the employee bonus of rate x salary and return this value. 
Demonstrate this method works by entering a bonus rate and displaying the bonus. 
'''

class Employee:

    def __init__(self, first, last, pay): 
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullName(self):
        return "{} {}".format(self.first, self.last)
    
    def bonus(self, rate):
        b = float(rate) * float(self.pay)
        return b
    
emp_1 = Employee("Kevin", "Ap", 60000.00)
emp_2 = Employee("Test", "User", 45000.00)

print(emp_1.email)
print(emp_2.fullName())
print(emp_1.first)
print(emp_1.last)
print(emp_1.pay)
print(emp_1.bonus(0.10))
print(emp_1.bonus(0.20))

