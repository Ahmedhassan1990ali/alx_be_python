monthly_income =int(input("Enter your monthly income: "))
monthly_expense =int(input("Enter your total monthly expenses: "))
month_savings= monthly_income -monthly_expense
projected_saving= month_savings *12 *1.05
print ("Your monthly savings are $", month_savings)
print ("Projected savings after one year, with interest, is: $", projected_saving) 