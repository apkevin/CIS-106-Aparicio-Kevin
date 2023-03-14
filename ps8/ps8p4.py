f = open("p8t4.txt", "r")


#intitalize counters and sums to 0
c = 0.0
total_ext = 0.0

# Get first Data line
item = str(f.readline().rstrip('\n'))

while item != "":
    
    qty = float(f.readline())
    price = float(f.readline())

    ext_price = qty * price
    # Sum and count - in the loop
    total_ext = total_ext + ext_price
    c = c + 1

    # Display a line of data
    print("item is: ", item)
    print("Quantity is: ", qty)
    print("Price is: ", price)
    print("Extended Price is: ", format(ext_price, '.2f'))

    # Get next data
    item = str(f.readline().rstrip('\n'))

# After the loop
# Final Calculations / Display them

print("Total Extended Prices: ", format(total_ext, '.2f'))
print("Number of Orders: ", c)
avg = total_ext / c
print("Average Order: ", format(avg, '.2f'))

