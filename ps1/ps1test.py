#function to calculate the current state of savings each month
def savings_36_months(current_savings, annual_salary, semi_annual_raise, portion_saved):
    '''Assume that arguments are floats
    returns the current savings under 36 months
    '''
    months = 0
    monthly_salary = annual_salary / 12

    while months < 36:
        current_savings += (monthly_salary * portion_saved) + (current_savings * r / 12)
        months += 1

        if months % 6 == 0:
            annual_salary += semi_annual_raise % annual_salary
            monthly_salary = annual_salary / 12.0
    #print(current_savings, months)
    return current_savings

#function to calculate the best saving rate with bisection search
def best_rate(current_savings, savings, savings_rate, low, high, epsilon, down_payment, num_guesses):
    '''assume the best rate is a float
    returns the best rate of savings
    '''
    if savings + epsilon <= down_payment:
        print('It is not possible to pay the down payment in three years.')
        exit()
    while abs(savings - down_payment) >= epsilon:
        if savings < down_payment:
            low = savings_rate
        else:
            high = savings_rate
        savings_rate = (high + low) / 2
        num_guesses += 1
        savings = savings_36_months(current_savings, annual_salary, semi_annual_raise, savings_rate)
        #print(savings)
    return savings_rate, num_guesses

annual_salary = float(input("Please, enter the starting annual salary: "))

semi_annual_raise = 0.07
down_payment = 1000000 * 0.25
current_savings = 0
r = 0.04
epsilon = 100
num_guesses = 0
low = 0
high = 1.0
savings_rate = (high + low) / 2.0
savings = savings_36_months(current_savings, annual_salary, semi_annual_raise, savings_rate)
best_rates, num_guesse = best_rate(current_savings, savings, savings_rate, low, high, epsilon, down_payment, num_guesses)


print('Best savings rate: ',round(best_rates, 4))
print('Steps in bisection search: ', num_guesse)
#print (current_savings, months)
