lastName = input("Enter your last name: ")
salary = int(input("Enter your Salary: "))
level = int(input("Enter your job level: "))

if level >= 10:
    bonusRate = .25
elif level >= 5 and level <= 9:
    bonusRate = .2
else:
    bonusRate = .1

bonus = salary * bonusRate

print(lastName)
print("Bonus: $" + str(bonus))