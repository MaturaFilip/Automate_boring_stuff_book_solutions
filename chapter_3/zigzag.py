"""Attempt to recreate zigzag program from book Automate the boring stuff with python"""

import time, sys

indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end=" ")
        print('********')
        time.sleep(0.1)

        if indentIncreasing:
            indent += 1
            if indent == 20:
                indentIncreasing = False

        else:
            indent -= 1
            if indent == 0:
            # change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()




