amount = input("Enter the quantity amount: ")
quantity = int(amount)

if quantity >= 1000:
    price = 3.00
else:
    price = 5.00

ext_Price = quantity * price
tax = round(ext_Price * .07, 2)
total = ext_Price + tax

print("Quantity:" + str(quantity))
print("Unit Price: $" + str(price))
print("Extended Price: $" + str(ext_Price)) 
print("Tax: $" + str(tax))
print("Total: $" + str(total)) 

