# In this assignment you will be tasked with finding the maximum and
# minimum values of a list, as well as its average.

# Here is the list in question:
list_one = [4, 58, 55, 94, 11, 89, 69, 12, 97, 2, 38, 20, 25, 6, 95, 89, 11, 89, 19, 85, 44, 28, 6, 86, 96, 21,
            11, 84, 52, 9, 19, 11, 57, 35, 76, 74, 46, 3, 72, 99, 15, 27, 40, 98, 53, 94, 21, 44, 112, 92]


# To find each value you will need to have a new For Loop,
# and use a few If Statements as well. No max() or min() functions
# allowed though, that'd be too easy.


# First Loop Here:
max = 0
for n in list_one:
    if n > max:
        max = n

# Second Loop Here:
min = 10
for n in list_one:
    if n < min:
        min = n

# Third Loop Here:
list_total = 0
list_elements_total = 0

for n in list_one:
    list_total += n

for elements in list_one:
    list_elements_total += 1

# Here are the variables to store your answers in:
list_max = max
list_min = min
list_average = list_total / list_elements_total
print(str(max))
print(str(min))
print(str(list_average))
















