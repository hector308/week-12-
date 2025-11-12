# Objective:
# Students will use logical (and, or, not) and chained comparison operators in Python to build compound conditions.

# Key Notes:

# and → Both conditions must be True

# or → At least one condition must be True

# not → Inverts True/False

# You can chain comparisons: 1 < x < 5

# Examples:
x = 10
print(x > 5 and x < 15)   # True
print(x < 5 or x == 10)   # True
print(not(x == 10))       # False
print(1 < x < 20)         # True

print("!")
# Practice Problems:

# Write an expression that checks if a number is between 50 and 100 (inclusive).
y=60
print(y>=50 and y<=100)
# Write an expression that checks if a number is NOT equal to 0 and greater than 10.
z=7
print(not(z==0 and z>=10))
# Use chained comparison to check if 3 < 4 < 5.
c=4
print (3<c<5)

# Challenge: Create a password rule using logical operators:

