"""
Sales Bonus
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, user gets a 10% bonus.
If sales are $1,000 and over, the bonus is 15%.

Pseudocode
get sales
while sales is > or = 0
    if sales is > or = 1000
        calculate 15% bonus
    else
        calculate 10% bonus
    display bonus
    get sales
"""
SENTINEL = 0
SALES_THRESHOLD = 1000
BONUS_15 = 0.15
BONUS_10 = 0.1

sales = float(input("Sales amount: "))
while sales >= SENTINEL:
    if sales >= SALES_THRESHOLD:
        bonus = sales * BONUS_15
    else:
        bonus = sales * BONUS_10
    print(f"For your sales of ${sales:.2f}, you have earned a bonus of ${bonus:.2f}.")
    sales = float(input("Sales amount: "))
