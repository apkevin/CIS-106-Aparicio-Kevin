name = input("Choose item A or item B: ")
amount = input("Please enter the quantity amount: ")
quantity = int(amount)
item = name.capitalize()
price = 0
ext_Price = 0

if item == "A":
    price = 10.00
elif item == "B":
    price = 20.00
else:
    print("Please type A or B ")

ext_Price = price * quantity

print("Item: " + item)
print("Price: $" + str(price))
print("Total: $" + str(ext_Price))
