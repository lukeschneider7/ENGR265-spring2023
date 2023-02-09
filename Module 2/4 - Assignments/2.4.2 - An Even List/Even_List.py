import random

"""
THIS SECTION IS DR. FORSYTH'S CODE. DO NOT MODIFY. BUT KEEP READING.
"""

# randomly sample a distribution between 2 and 6
random_number = int(random.uniform(2, 6))

# any number times 2 is even
an_even_number = 2 * random_number

# generate a random list of odd length containing values up to 100
even_list = random.sample(range(100), an_even_number)

# print out the list contents
print("Your list is: ", even_list)

"""
YOUR CODE BEGINS BELOW HERE. FILL IN THE MISSING OPERATIONS / CODE
"""
# Fine middle lower middle index
lower_middle_index = (len(even_list)/2) - 1

# Upper middle index (plus one because list slicing does include upper index)
upper_middle_index_plus_one = (len(even_list)/2) + 1

# List of middle elements, check to make sure it works
middle_elements = even_list[int(lower_middle_index):int(upper_middle_index_plus_one)]
print(middle_elements)

# this is the final result. Modify this line, and the empty lines above, to solve the assignment
middle_average = sum(middle_elements)/2



# The average of middle elements is
print("The average is: ", middle_average)
