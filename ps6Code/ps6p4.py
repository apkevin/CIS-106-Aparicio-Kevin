tickets = int(input("Enter number of tickets: "))

if tickets >= 25:
    pricePerTicket = 50.00
elif tickets >= 10 and tickets <= 24:
    pricePerTicket = 60.00
elif tickets >= 5 and tickets <= 9:
    pricePerTicket = 70.00
else:
    pricePerTicket = 75.00

total = pricePerTicket * tickets

print("Number of tickets: " + str(tickets))
print("Price per ticket: $" + str(pricePerTicket))
print("Total: $" + str(total))