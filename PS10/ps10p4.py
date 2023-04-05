'''
4.	Prompt the user to repeatedly to do the program( input (Yes or No)). 
If they response Yes go into the loop and prompt the user for last name and miles from downtown Chicago. 
Write a function to compute the train ticket price. 
Pass to the function the miles from down town Chicago and determine the ticket price. 
Return the ticket price. 
Sum price of all tickets. 
Miles from Down Town Chicago			Ticket Price
30 or more					     $12
20 to 29					     $10
10 to 19					     $8
All others					     $5

'''
def price(miles):
    if miles >= 30:
        ticket_Price = 12.00
    elif miles >=20 and miles <=29:
        ticket_Price = 10.00
    elif miles >= 10 and miles <= 19:
        ticket_Price = 8.00
    else:
        ticket_Price = 5.00

    return ticket_Price
# Initializing Summing
total_Amount = 0
while True:
    user_input = input("Do you want to run the program? (Yes/No)")

    if user_input.lower() == 'yes':
# The program will now run
        
        last_name = input("Enter your last name: ")
        miles = float(input("Enter how many miles away you are from downtown Chicago? "))

        amount = price(miles)
        total_Amount += amount

        print(f"The price of your train ticket for {last_name} is ${amount}")
        print(f"Total Amount for everybody will be ${total_Amount}")
    
    elif user_input.lower() == 'no':

        print("PROGRAM WILL NOW CLOSE. ")
# Loop will stop running
        break
    
    else:
        print("Please type Yes or No. ")