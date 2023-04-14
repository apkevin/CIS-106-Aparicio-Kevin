def discount(qty, price, discount_Rate):
    total = (qty * price)
    discount_Amount = (discount_Rate / 100) * total
    discount_Price = total - discount_Amount

    return discount_Amount, discount_Price

qty = float(input("Enter the quantity: "))
price = float(input ("Enter the unit price: $"))
discount_Rate = float(input("Enter the discount rate: %"))
discount_Amount, discount_Price = discount(qty, price, discount_Rate)

print(f"Quantity is {qty}")
print(f"Unit price ${price}")
print(f"Discount ${discount_Amount}")
print(f"Price with discount ${discount_Price}")
