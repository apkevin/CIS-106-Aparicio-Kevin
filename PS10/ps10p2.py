'''
2.	Prompt the user to repeatedly to do the program( input (Yes or No)). 
If they response Yes go into the loop and prompt the user for length, width and height of a room. 
Write a function to compute the square footage of the room. 
The function should receive the length, width and height of the room and 
return square footage (2 x length x width (floor and ceiling) + 2 x length x height (2 of the walls) + 2 x width x height (the other 2 walls). 
A gallon of paint covers 50 square feet. 
Compute the number of gallons needed to paint the room (square footage of the room / 50). 
Display the number of gallons needed. 
'''
def square_footage(lenght, width, height):
    square_feet = (2 * lenght *  width) + (2 * lenght * height) + (2 * width * height)

    return square_feet


while True:
    user_input = input("Do you want to run the program? (Yes/No)")

    if user_input.lower() == 'yes':
# The program will now run

        length = float(input("Type the length: "))
        width = float(input("Type the width: "))
        height = float(input("Type the height: "))

# Calling Function
        square_feet = square_footage(length, width, height)

# Printing Results
        print(f"The room has {square_feet} square feet")

    elif user_input.lower() == 'no':

        print("PROGRAM WILL NOW CLOSE. ")
# Loop will stop running
        break
    
    else:
        print("Please type Yes or No. ")
