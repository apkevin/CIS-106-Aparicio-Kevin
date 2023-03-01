principle = int(input("Enter Principle amount: "))
year = int(input("Enter years to maturity: "))

if principle > 100000 and year == 5:
    interestRate = .06
elif principle >= 50000 and principle <= 100000 and year == 10:
    interestRate = .05
elif principle >= 50000 and principle <= 100000 and year == 5:
    interestRate = .04
else:
    interestRate = .02

interest = principle * interestRate
percent = interestRate * 100

print("Principle: $" + str(principle))
print("Interest Rate: " + str(percent) + "% ")
print("Interest Total: $" + str(interest))
