"""
individual_error-fixing1.py

This program calculates the monthly mortgage payment for a fixed-cost house.
It defines a function to compute the payment based on the principal amount,
annual interest rate, and the duration of the loan in years. The user is prompted
to enter the number of years they wish to take to pay off the mortgage, and the
program outputs the corresponding monthly payment formatted as a monetary value.
"""
# +-----------------------------+
# |   O                         |
# |  /|\                        |
# |   |    Fix my code          |
# |  / \   please. It's         |
# |        giving me an error!! |
# +-----------------------------+

def calculate_monthly_payment(principal, annual_interest_rate, years):
    
    monthly_interest_rate = annual_interest_rate / 12 / 100
    number_of_payments = years * 12
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
    return monthly_payment

def main():
    principal = 300000  # Fixed cost of the house
    annual_interest_rate = 3.5  # Fixed annual interest rate

    years = int(input("Enter the number of years you want to pay off the mortgage: "))

    monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)
    print(f"Your monthly payment will be: ${monthly_payment:.2f}")

if __name__ == "__main__":
    main()