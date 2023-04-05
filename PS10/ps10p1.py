# Generating forcast
def forecast(month, sales):
    if month.lower == "january" or "february" or "march":
        percent = 0.10
    elif month.lower == "april" or "may" or "june":
        percent = 0.15
    elif month.lower == "july" or "august" or "september":
        percent = 0.20
    elif month.lower == "october" or "november" or "december":
        percent = 0.25
    else:
        print("Please type in a valid month")
            
    sales = sales * (1 + percent)

    return sales
while True:
    # Asking User if they want to run the loop on the program
    user_input = input("Do you want to run the program? (Yes or No): ")

    if user_input.lower() == "yes":
        
        #Program will run
        # Retreiving information for the function
        last_name = input("Enter your last name. ")
        month = input("Enter a month. ")
        sales = float(input("Enter the amount of sales. "))

        # Calling Function
        next_Month_sales = forecast(month, sales)

        # Printing Results
        print("Next month's sales will be {:.2f}".format(next_Month_sales))

    elif user_input.lower() == "no":
        print("Leaving Program.")
        break #Exiting LOOP
    else:
        print("Please type in 'Yes' or 'No'.")    

