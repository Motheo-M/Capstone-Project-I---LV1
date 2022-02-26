import math  # import be able to make complex math calculations

# The formulas are on continued in new lines.
# Due to them being longer than 79 characters.
# Will input whether we want to calculate bond owed or investment profits
sentence = input("Choose either 'investment' or 'bond' from"
                 " the menu below: \n"
                 "investment \t - to calculate the amount of"
                 " interest you'll earn on interest \n"
                 "bond \t \t - to calculate the amount"
                 " you'll have to pay on a home loan \n \n" 
                 "Please type your choice to proceed: ")

# Prints the message in capital
# Regardless of whether input is lower or uppercase.
message = sentence.upper()
print(message)

# If we choose INVESTMENT.
# We will input amount we want to deposit.
# Then we will input the rate of interest of deposit.
# Then the number of years our deposit will be invested for.
# Then should our deposit be simple interest or compound interest.
# Then we'll receive a print out of the total investment based on our choice.
# If inputs are invalid, a message will be printed to let the user know.
if message == "INVESTMENT":
    amount_deposit = float(input("Enter the amount you want to deposit: "))
    amount_int_rate = float(input("Enter the interest rate(%) of deposit: "))
    amount_years = float(input("Enter the number of years the"
                               " deposit will be invested for: "))
    interest_sentence = input("Do you want simple or compound interest? \n"
                              "Please enter your choice: ")
    interest_message = interest_sentence.upper()

    # SIMPLE and COMPOUND interest calculation formula.
    if interest_message == "SIMPLE":
        amount_calculated = amount_deposit * (1 + ((amount_int_rate / 100)
                                                   * amount_years))
        print(amount_calculated)
    elif interest_message == "COMPOUND":
        amount_calculated = amount_deposit \
                            * math.pow((1 + amount_int_rate / 100),
                                       amount_years)
        print(amount_calculated)
    else:
        print("This is an invalid input. Please type valid input to proceed.")

# BOND is calculated using the formula below.
# The current value of the house is entered.
# The current yearly interest rate of the house is entered.
# The number of months left to repay the bond at the expected time.
# The amount to be paid each month to pay off the BOND is calculated.
# It will be printed in the terminal.
# If inputs are invalid, a message will be printed to let the user know.
elif message == "BOND":
    house_value = float(input("Enter the present value of the house: "))
    house_int_rate = float(input("Enter the interest rate(%) of the bond: "))
    house_mon_rate = house_int_rate / 12
    house_months = float(input("Enter the number of months"
                               " left to pay off bond: "))
    amount_calculated_top = house_mon_rate * house_value
    amount_calculated_bottom = 1 - math.pow(1 + house_mon_rate,
                                            - house_months)
    amount_calculated = amount_calculated_top / amount_calculated_bottom
    print(amount_calculated)
else:
    print("This is an invalid input. Please type valid input to proceed.")

# REFERENCE
# NONE
