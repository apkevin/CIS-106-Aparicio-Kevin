meal_total = input("How much was to total price for your meal? ");

#Converting meal into a float number
meal = float(meal_total);

# Adding tips
tip_15 = round((meal * .15), 2);
tip_18 = round((meal * .18), 2);
tip_20 = round((meal * .2), 2);

# Making seperate variables for summming up to the total and tip
total_15 = meal + tip_15;
total_18 = meal + tip_18;
total_20 = meal + tip_20;

# Display receipt with different tip options. 
print("With 15% Tip: \n");
print("Total $", meal);
print("Tip $", tip_15);
print("Total with Tip $", total_15);

print("With 18% Tip: \n");
print("Total $", meal);
print("Tip $", tip_18);
print("Total with Tip $", total_18);

print("With 20% Tip: \n");
print("Total $", meal);
print("Tip $", tip_20);
print("Total with Tip $", total_20);