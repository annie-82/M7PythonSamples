# -------------------- PROBLEM 2 --------------------
# prompt the user to enter a number
number = int(input('Enter a number to check in range(1, 10) : '))

# check if 'number' lies between 1 and 10
if number >= 1 and number <= 10:                  # SUPPOSED TO USE IN, NOT IN OPERATOR
    # if it is in range, print apt message        #if number in range(1, 11):
    print('The number is in range(1,10)')

else:
    # if it is NOT in range, print apt message
    print('The number is NOT in range(1,10)')
