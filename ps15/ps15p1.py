'''
1.	Starting with the employee class you created in the previous assignment, 
create a manager class. This class should use the previously created employee class as the base class and make a derived class called manager. 
This class should include a long term bonus method that compute the long term bonus to be 40% of their salary. 
Create a program to instantiate the new class and show that it works. 
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

class Manager(Employee): 
    
    def long_bonus(self):
        c = .40 * float(self.pay)
        return c


emp_1 = Employee("Kevin", "Ap", 60000.00)
emp_2 = Employee("Test", "User", 45000.00)
mgr_1 = Manager("Eric", "M", 80000.00)


print(emp_1.email)
print(emp_2.fullName())
print(emp_1.first)
print(emp_1.last)
print(emp_1.pay)
print(emp_1.bonus(0.10))
print(emp_1.bonus(0.20))

print(mgr_1.long_bonus())
print(mgr_1.first)