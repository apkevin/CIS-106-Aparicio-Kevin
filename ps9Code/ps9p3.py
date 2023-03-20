city = input("Name of city: ")
miles = float(input("Number of miles traveled: "))
gallons = float(input("amount of gallons used: "))

def compMpg(miles, gallons):
    mpg = miles / gallons
    return mpg

def compCost(gallons):
    cost = gallons * 2.50
    return cost

mpg = compMpg(miles, gallons)
cost = compCost(gallons)

print("Destination: ", city)
print("Miles per Gallon: ", mpg)
print("Cost: $", cost)