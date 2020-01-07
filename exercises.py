# Question 1
# Assume a population of rabbits doubles every 3 months. How many rabbits after 2 years? Initial population is 11

# First, set up all the required variables
initial_number_of_rabbits = 11
pop_growth_rate_months = 3
time_frame_years = 2

# change time frame from years to months
time_frame_months = time_frame_years * 12

# create script to calculate the final rabbit population
final_population = initial_number_of_rabbits * (time_frame_months // pop_growth_rate_months)

# Print answer
print(F"The final population is: {final_population}")

# Question 2
# Same as question one, except include a user input for the initial number of rabbits and time frame

initial_number_of_rabbits = int(input("How many rabbits are there to start? "))
time_frame_years = int(input("How long will you have them? "))
time_frame_months = time_frame_years * 12

# This script should be saved as a function instead so that it can be reusable
final_population = initial_number_of_rabbits * (time_frame_months // pop_growth_rate_months)

print(F"The final population is: {final_population}")

# Question 3
# Assume the user is going to input 2 numbers, x and y for example. Write a Python program that will swap the numbers stored in these variables
x = 3
y = 11
u = x
v = y
y = u
x = v
print(f"{x} and {y}")

# Question 4
# The goal of this task is to derive a single assignment statement for the following sequences such that, if the variable x has the first value in a sequence, then x will have the next value in the sequence after the assignment statement is executed. And if the assignment statement were executed repeatedly, then x would cycle through all of the values in the sequence.

# first series: 0 2 4 6 8
x = 0
x = x + 2

# second series: 0 -1 -2 -3 -4
y = 0
y = y -1

# Third series: 6 -6 6 -6 6 -6
z = 6
z = z/-1

# Forth series: 0 3 6 0 3 6 0 3 6
a = 0
a = a + 3

