name = input("Plase enter your name: ")
cost = float(input("Please enter the cost of the item: "))
warranty = 0
total_Warranty = 0
total = 0

if cost >= 1000:
    warranty = .1
elif cost < 1000:
    warranty = .05

total_Warranty = cost * warranty
total = cost + total_Warranty

print("Name: " + name)
print("Cost: $" + str(cost))
print("Cost of Warranty: $" + str(total_Warranty))
print("Total Cost: $" + str(total))