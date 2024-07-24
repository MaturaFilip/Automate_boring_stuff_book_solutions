"""How to terminate program before the last instruction"""

import sys

while True:
    print(f"Type exit to exit.")
    response = input()
    if response == "exit":
        sys.exit()
    print(f"You typed {response}.")