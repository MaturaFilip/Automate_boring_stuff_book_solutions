"""Practice project for chapter 3 from the book Automate the boring stuff with python"""

import sys, time

# function collatz()
def collatz(number):
    if number % 2 == 0:
        return (number // 2) # without reminder
    elif number % 2 == 1:
        return (3 * number + 1)


print('Enter number:')
try:
    user_input = int(input('>\n'))
except ValueError:
    print('You must enter an integer!')

try:
    while user_input != 1 or user_input < 1:
        user_input = collatz(user_input)
        print(user_input)
        time.sleep(0.1)
except NameError:
    print('')
