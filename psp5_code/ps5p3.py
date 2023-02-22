quantity = int(input("Enter Quantity: "))
cost = float(input("Enter cost of item: $"))
shipping = 0
total = cost * quantity

if total >= 50.00:
    shipping = 0
elif total < 50.00:
    shipping = 25.00

ext_Total = total + shipping

if shipping == 0:
    shipping = "Free"

print("Total: $" + str(ext_Total))
print("Shipping: " + str(shipping))