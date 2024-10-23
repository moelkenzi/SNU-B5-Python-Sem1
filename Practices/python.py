# Printing the welcome message
print(' ')
print('------- SNUSC -------')
print(' ')

# Taking user name as input
name = input('First, Enter your name:- ')

# Using try-except to handle potential errors
try:
    # print(hioens)
    ID = input('Your Std. Id :- ')  # Taking user ID input
    ID = int(ID)  # Converting ID to an integer
except ValueError:  # Correctly spelled 'except'
    print(' ')
    print('Please enter a valid number for the ID')

# Displaying the final message
print(' ')
print('Hi👋 ' + name + ',\nwelcome to the SNUSC, the most powerful and intellectual Club for the Somali National Student Club.' + '\nYour Id is :- ' + str(ID))
print('                 ')
print('------- SNUSC -------')

