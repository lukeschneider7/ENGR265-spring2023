"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 1-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $44B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
"""

### all your code below ###

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

# final answer for 10-year
ten_year_final = ten_year_value

# final answer for 20-year
twenty_year_final = twenty_year_value

