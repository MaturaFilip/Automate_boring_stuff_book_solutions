#!/usr/bin/python3

import pyinputplus as pyip

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt, yesVal = 'ano', noVal = 'ne') # allow czech lang

    if response == 'no' or response == 'ne': # the YesNo react only to yes, no but also for n and y
        break

print('Thank you. Have a nice day.')
