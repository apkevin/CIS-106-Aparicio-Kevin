# Read and open file
f = open("p8t5.txt", 'r')

# Declare conter and Total Tuition cost
c = 0
total = 0.00

# Read first line
last_name = str(f.readline().rstrip('\n'))

# Loop to get students tuition rates and credits taken
while last_name != "":

    district = str(f.readline().rstrip('\n'))
    credits = float(f.readline())

    if district == "I":
        cost_per_credit = 250.00
    else:
        cost_per_credit = 500.00
    
    tuition = cost_per_credit * credits
    c = c + 1
    total = total + tuition

    print("Last Name: ", last_name)
    print("Credits: ", credits)
    print("Tuition Total: $", tuition)

    last_name = str(f.readline().rstrip('\n'))

print("Number of students: ", c)
print("Total Tuition Owed: $", total)