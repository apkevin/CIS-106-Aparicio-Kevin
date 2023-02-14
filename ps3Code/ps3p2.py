

price_share = input("Enter the price per share of the stock: ");
current_stock = input("Enter the current stock price: ");
quantity_stock = input("Enter quantity amount of stocks: ");

# Converting inputs into float numbers
price_per_share = float(price_share);
current_price = float(current_stock);
quantity = float(quantity_stock);

# Calculating increase
calculate = (current_price - price_per_share) * quantity;

# Rounding the value
value = round(calculate, 2);

# Determining whether the value has gone up or down. 
if value > 0:
    print("You are making money! $" + str(value))
else:
    print("You are losing money! $" + str(value))