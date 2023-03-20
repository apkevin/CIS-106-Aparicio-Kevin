lastName = input("Player last name: ")
hits = float(input("how many hits did they record? "))
bats = float(input("Number of at bat attempts: "))

#Initializing function to determine batting avg
def compAvg(hits, bats):
    
    avg = hits / bats
    return avg

# Call Function
avg = compAvg(hits, bats)

#Display Results
print(lastName)
print("Avg: ", "%.3f" % avg)
