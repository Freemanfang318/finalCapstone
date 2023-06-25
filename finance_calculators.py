import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed:")


if user_input.lower().strip() == "investment":      # to lower and trim the input string
    inv_money = float(input("Please input the amount of money deposit: "))
    inv_interest = float(input("Please input the interest rate in number only: "))
    inv_year = float(input("How many years are you investing?:"))
    interest = input("Please select 'simple' or 'compound' interest:")
    if interest.lower().strip() == "simple":        # to lower and trim the input string
        total_money = inv_money * (1+(inv_interest/100)*inv_year)
        print(f"You can get ${total_money}")
    elif interest.lower().strip() == "compound":    # to lower and trim the input string
        total_money = inv_money * math.pow((1+(inv_interest/100)),inv_year)
        print(f"You can get ${total_money}")
    else:
        print("Wrong selection")

elif user_input.lower().strip() == 'bond':          # to lower and trim the input string
    house_price = float(input("Please enter your house price:"))
    bond_interest = float(input("Please enter the interest rate:"))
    bond_time = float(input("Please enter the length of repayment in month:"))
    bond_interest2 = bond_interest/100


    repayment_value = (bond_interest2*house_price) / (1 - (1+bond_interest2)**(-bond_time))
    print(f"Your repayment in each month is ${repayment_value}")
else:
    print("Wrong Selection")

