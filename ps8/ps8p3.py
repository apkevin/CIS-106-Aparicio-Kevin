# Reading File
f = open("p8t3.txt", "r")

# Retrieving first line
item = str(f.readline().rstrip('\n'))

while item != "":

    salary = float(f.readline())

    #calculating bonus
    if salary > 99999.99:
        bonus_rate = .20
    elif salary >= 50000 and salary <=99999.99:
        bonus_rate = .15
    elif salary <50000:
        bonus_rate = .10
    
    bonus = salary * bonus_rate

    print("Last Name ", item)
    print("Salary $", salary)
    print("Bonuse $", bonus)

    # Read next line of data
    item = str(f.readline().rstrip('\n'))

