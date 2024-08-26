#!/usr/bin/python3
import random

numberOfStreaks = 0
for experimentNumber in range(10_000):
    # code that creates a list of 100 'heads' or 'tails'
    flips = []
    for i in range(100):
        if random.randint(0,1):
            flips.append('H')
        else:
            flips.append('T')


    # Code that checks if there is a streak of 6 heads or tails in a row
    for i in range(100 - 6):
        if flips[i] == flips[i+1] == flips[i+2] == flips[i+3] == flips[i+4] == flips[i+5]:
            numberOfStreaks += 1
            break

print(f'Chance of streak: {numberOfStreaks / 10_000}')


# message='looool'
# for i in range(len(message)):
    # chunk = message[i:i+12]
