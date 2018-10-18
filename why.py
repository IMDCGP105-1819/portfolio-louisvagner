month_counter = 0
portion_deposit = 0.20
current_savings = 0
r = 0.04


annual_salary = input ("Please enter your current annual salary: ")
portion_saved = input ("Please enter how much you would like to be saved, as a decimal: ")
total_cost = input ("Please enter the cost of your dream home: ")

annual_salary = int(annual_salary)
portion_saved = float(portion_saved)
total_cost = float(total_cost)

monthly_salary = annual_salary/12 

while current_savings != total_cost:

    current_savings = monthly_salary + (monthly_salary/r)
    month_counter = month_counter + 1
    
    if current_savings == total_cost:
        print (current_savings)
        print (total_cost)


    else:
        print (current_savings)
        print (total_cost)

