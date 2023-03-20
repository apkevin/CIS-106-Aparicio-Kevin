# Defining Variables
qty = float(input("Enter quantity: "))
price = float(input("Enter price: "))

# Function to calculate total
def sumTotal(qty, price):

    total = qty * price

    if total > 10000.00:
        total = total = total * .9
    return total

total = sumTotal(qty, price)

# Printing Valuies
print("Quantity: ", qty)
print("Price: $", price)
print("Total: $", total)

