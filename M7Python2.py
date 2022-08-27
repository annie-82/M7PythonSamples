# -------------------- PROBLEM 2 --------------------
# prompt the user to enter a number

'''
# Problem 2: Write a Python function to check whether a number is in a given range. Use range(1,10).
# Print whether the number is in or not in the range.
'''

number = int(input('Enter a number to check in range(1, 10) : '))

# check if 'number' lies between 1 and 10
if number >= 1 and number <= 10:                #if number in range(1, 10):
    # if it is in range, print apt message
    print('The number is in range(1,10)')

else:
    # if it is NOT in range, print apt message
    print('The number is NOT in range(1,10)')
