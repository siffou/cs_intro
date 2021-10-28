#input to collect informations from user
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

#instantiation of known variables
portion_down_payment = 0.25
current_savings = 0
r = 0.04
months = 0

#how much is down_payment
down_payment = total_cost * portion_down_payment
savings = (annual_salary*r/12) + (portion_saved*(annual_salary/12))

#how much do you save a month
while current_savings < down_payment:
    current_savings += (current_savings*r/12) + (portion_saved*(annual_salary/12))
    #counter to follow up
    months += 1
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise

print("Number of months:", months)
print("Current savings:", current_savings)
print(down_payment / savings)
