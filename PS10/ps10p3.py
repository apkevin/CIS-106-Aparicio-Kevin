'''
3.	Prompt the user to repeatedly to do the program (input (Yes or No)). 
If they response Yes go into the loop and prompt the user for make, model, electric vehicle code (Y or N) and 
MSRP (sticker price) of an automobile. Write a function to compute the out the door price. 
Pass to the function the MSRP, make, model and electric vehicle code. Determine the percent off the MSRP
 then compute the new MSRP and finally add 7% sales tax to the total. Return and display the total. 
Also sum all MSRP’s and sum of all sales price of the cars (MSRP – discount + tax).
'''
def price(msrp, make, model, electric_code):
    if make.lower() == "honda" and model.lower() == "accord":
        percent_off = 0.10
    elif make.lower() == "toyota" and model.lower() == "rav4":
        percent_off = 0.15
    elif electric_code == "yes":
        percent_off = 0.30
    else:
        percent_off = 0.05
    
    discount = msrp * percent_off
    new_msrp = msrp - discount
    tax = new_msrp * .07
    total = msrp - discount + tax

    return total
while True:
    user_input = input("Do you want to run the program? (Yes/No)")

    if user_input.lower() == 'yes':
# The program will now run
        make = input("Enter the make of the vehicle: ")
        model = input("Enter the model of the vehicle: ")
        electric_code = input("Enter if vehicle has an electric vehicle code: (Yes/No) ")
        msrp = float(input("Enter the MSRP price of the vehicle: "))

# Calling Function
        
        sum = price(msrp, make, model, electric_code)

        print(f"The total amount for the vehicle is ${sum}. ")

    elif user_input.lower() == 'no':

        print("PROGRAM WILL NOW CLOSE. ")
# Loop will stop running
        break
    
    else:
        print("Please type Yes or No. ")

