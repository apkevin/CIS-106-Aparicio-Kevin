'''
5.	
Prompt the user to repeatedly to do the program( input (Yes or No)). 
If they response Yes go into the loop and prompt the user for county and market value of a home. 
Write a function to compute the assessed value. Pass to the function the county and market value. 
The function will determine the assessed value percent then compute and return the assessed value. 
(Multiple the market value by assessed value percent. Sum and display all market values and assessed values. 

County		Assessed Value Percent
Cook		        0.90
DuPage		        0.80
McHenry		        0.75
Kane		        0.60
All others		       0.70

'''
def value(county, market_Value):
    if county.lower() == "cook":
        percent = 0.90
    elif county.lower() == "dupage":
        percent = 0.80
    elif county.lower() == "mchenry":
        percent = 0.75
    elif county.lower() == "kane":
        percent = 0.60
    else:
        percent = 0.70

    asessed_Value = market_Value * percent 
    return asessed_Value

# Initializing counter
total_Value = 0

while True:
    # Asking User if they want to run the loop on the program
    user_input = input("Do you want to run the program? (Yes or No): ")

    if user_input.lower() == "yes":
    # Executing Code
        county = input("Enter the name of the county: ")
        market_Value = float(input("Enter the market value of the home: "))

        asessed_Value = value(county, market_Value)
        total_Value += asessed_Value

        print(f"The markete value of this home located in {county} county is, ${asessed_Value}")
        print(f"The toal value for all the homes is, ${total_Value}")

    elif user_input.lower() == "no":
        print("Leaving Program.")
        break #Exiting LOOP
    else:
        print("Please type in 'Yes' or 'No'.")  