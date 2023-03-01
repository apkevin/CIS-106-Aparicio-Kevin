partNumber = int(input("Enter part number: "))
quantity = input("Enter Quantity: ")

if partNumber == 10 or partNumber == 55:
    cost = 1.00
elif partNumber == 90:
    cost = 2.00
elif partNumber == 80 or partNumber == 70:
    cost = 3.00
else:
    cost = 5.00

total = cost * float(quantity)

print("Part Number: " + str(partNumber))
print("Cost Per Unit: $" + str(cost))
print("Total: $" + str(total))