import math

# Initial Variables for treasury bond duration and interest rate
principal = 44000000000
i1 = 3.96
n1 = 10
i2 = 4.32
n2 = 10

# Value of bonds after ten and twenty years respectively
ten_year_value = principal * ((1 + (i1/100)) ** n1)
twenty_year_value = principal * ((1 + (i2/100)) ** n2)

# Profit on bonds after ten and twenty years
ten_year_profit = ten_year_value - principal
twenty_year_profit = twenty_year_value - principal

# Showing Elon's ten-year profit as an integer
print("Elon's ten year profit on a $44 billion purchase of treasury bonds would be $", int(ten_year_profit))

# Showing Elon's twenty-year profit as a float
print("Elon's twenty year profit on a $44 billion purchase of treasury bonds would be $", float(twenty_year_profit))
