
annual_salary = input("What is your annual salary? : ")
portion_saved = input("what percentage of your salary to you save? : ")
real_total_cost = input("How much does the house you want to buy costs? : ")

portion_deposit = 0.20
current_savings = 0
annual_return = 0.04

#reduce the total price of the house using the portion_deposit
your_total_cost = float(real_total_cost)*portion_deposit

annual_salary = int(annual_salary)
portion_saved = float(portion_saved)
annual_return = float(annual_return)

monthly_salary = annual_salary/12

months_needed = 0

while current_savings < your_total_cost:
    months_needed = months_needed + 1
    current_savings = current_savings + (monthly_salary*portion_saved)
    current_savings = current_savings+(current_savings*(annual_return/12))

print(f"You will need to save for {months_needed} months to buy the house.")
