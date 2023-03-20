lastName = input("Enter last name: ")
credit = float(input("Amount of credit hours: "))
district = input("Enter district code: ")

def compTuition(credit, district):

    if district == "I":
        tuition = 250.00 * credit
    else: 
        tuition = 550.00 *  credit
    return tuition

tuition = compTuition(credit, district)

print(lastName)
print("Tution Total: $", tuition)