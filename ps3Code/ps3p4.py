first_name = input("What is your name? ");
steps_walked = input("How many steps have you walked today? ");

# Converting steps walked into a number
steps = float(steps_walked);

# Calculating how many calories the user has burned
burned = steps * .25;

# Rounding variable burned to 2 decimal places. 
calories = round(burned, 2);

# Displaying Output
print(first_name + ", you have burned a total of " + str(calories) +" calories today. ");
