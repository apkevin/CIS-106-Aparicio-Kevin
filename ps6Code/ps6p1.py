quantity = int(input("Please enter the Quantity: "))
price = float(0)
tax = float(0.07)

if quantity > 10000:
        price = 10.00
elif quantity >= 5000 and quantity <= 10000:
        price = 20.00
elif quantity < 5000:
        price = 30.00

extPrice = quantity * price
taxAmount = tax * extPrice
total = extPrice + taxAmount

print("Subtotal: $" + str(extPrice))
print("Tax: $" + str(taxAmount))
print("Total: $" + str(total))