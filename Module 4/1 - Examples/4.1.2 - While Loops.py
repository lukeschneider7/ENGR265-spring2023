# The second type of loop is known as a while loop!
# The easy way to think of these is while some condition
# is true, keep running. Let's take a look:

iterations = 1

while iterations <= 5:
    # print("This has looped " + str(iterations) + " times.")
    iterations += 1

# Notice how after iterations got above 5 it stopped?
# That is because the while loop's condition was no
# longer true.

# In addition to having some condition in the creation
# of the loop, you can have a condition inside the loop
# to break out if need be.

# Comment out the above print statement and uncomment the next two.

exponential_growth = 1

while True:
    exponential_growth *= 2
    if exponential_growth > 200:
        print(str(exponential_growth) + " is too Big!!! Stopping!!!")
        break
    print(exponential_growth)

end_line = -1


python_hours = 16
week = 3

while True:
    python_hours += 6
    week += 1
    if python_hours > 100:
        print("You've put in:", str(python_hours), "hours of python coding, meeting the requirements of this course.")
        print("It took you:", str(week), "weeks")
        break
    print("week", str(week), str(python_hours), "python hours put in")

# One thing to note: if a while loop is poorly defined it can
# easily become infinite and run forever. If this ever happens,
# press the red button in the terminal, or close PyCharm.
