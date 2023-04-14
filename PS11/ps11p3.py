#Function
def calculate_comission(sales):

    if sales > 100000:
        percent = .10
    elif sales <= 100000:
        percent = .05
    
    comission = sales * percent
    next_year = sales * 1.05

    return comission, next_year

last_name = input("Enter the sales person last name: ")
sales = float(input("Enter sales amount: $"))

comission, next_year = calculate_comission(sales)

print(f"Comission: ${comission}")
print(f"Projections: ${next_year}")
