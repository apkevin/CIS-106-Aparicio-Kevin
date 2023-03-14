
principle = float(input("Enter Principle: "))
int_rate = float(input("Enter interest rate: "))

for year in range(1, 6, ):

# Calculating interest amount

    interest = principle * int_rate
    ending_bal = principle + interest
    print(year, "    ", principle, "    ", ending_bal)
    principle = ending_bal



