start = int(input("Enter your starting value:"))
stop = int(input("Enter your stopping value:"))
increment = int(input("Enter increment value"))

# Checking if stopping value is greater than starting value.
''' if stop < start:
    print("STOP VALUE HAS TO BE GREATER THAN START VALUE!!")'''

while start <= stop:

    print(start)
    start = start + increment
