lastName = input("Last Name: ")
jobCode = input("Job Code: ")
hours = float(input("Hours Worked: "))

def pay(jobCode):

    if jobCode == "L":
        payRate = 25.00
    elif jobCode == "A":
        payRate = 30.00
    else:
        payRate = 50.00
    
    return payRate
def compGross(hours, payRate):
    if hours > 40:
        grossPay = (hours - 40) * payRate * 1.5 + (40 * payRate)
    else:
        grossPay = hours * payRate
    return grossPay

payRate = pay(jobCode)
grossPay = compGross(hours, payRate)

print(lastName)
print("Gross, Pay: $", grossPay)

