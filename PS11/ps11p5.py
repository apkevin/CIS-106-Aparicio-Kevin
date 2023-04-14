total = 0
tax = 0

def total_price(quantity, price):
    global total
    total = quantity * price
    global tax 
    tax = total * .07

    return 

quantity = float(input("Enter quantity: "))
price = float(input("Enter price: $"))

total_price(quantity, price)

print(f"Total: ${total}")
print(f"Tax: ${tax}")