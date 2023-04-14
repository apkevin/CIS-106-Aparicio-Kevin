# fUNCTION
def grade(test1, test2, test3):
    
    total_points = test1 + test2 + test3
    avg = (test1 + test2 + test3) / 3

    return total_points, avg


# Input information
last_name = input("Enter your last name: ")
test1 = float(input("Enter first test score: "))
test2 = float(input("Enter second test score: "))
test3 = float(input("Enter third test score: "))

total_points, avg = grade(test1, test2, test3)

#Output
print(f"{last_name} your avg test score is {avg}, and {total_points} is your total amount of points. ")



