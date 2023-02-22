lastName = input("Enter your Last Name: ")
dependents = int(input("Enter the number of Dependents: "))
grossIncome = int(input("Enter your Gross Income: "))
adjusted = grossIncome - (dependents * 1200)
taxRate = 0
incomeTax = 0

if adjusted >= 50000:
    taxRate = .2
elif adjusted > 0 and adjusted <= 50000:
    taxRate = .1
elif adjusted < 0:
    incomeTax = 100

incomeTax = adjusted * taxRate

print("Last Name: " + lastName)
print("Gross Income: $" + str(grossIncome))
print("Number of Dependents: " + str(dependents))
print("Adjusted Gross Income: $" + str(adjusted))
print("Income Tax: $" + str(incomeTax))
