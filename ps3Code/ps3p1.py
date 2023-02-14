import math

exam1 = input("Enter test score #1 ");
exam2 = input("Enter test score #2 ");

# converting inputs into integers for multiplication to be possible. 
test1 = float(exam1);
test2 = float(exam2);

# calculating logic into variable grade. 
grade = (test1 * .6) + (test2 * .4);

# Rounding variable grade so it doesn't include all the decimals. 
score = math.floor(grade);

# Printing final score. 
print("Your final grade is " + str(score));