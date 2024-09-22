#!/usr/bin/env python3
import sys

# Author: Arshdeep Singh
# Author ID: aswalia6
# Date Created: 2024/09/21

# Assign the first command-line argument to the variable timer
timer = int(sys.argv[1])

# Loop until the timer reaches 0
while timer > 0:
    print(timer)
    timer -= 1  # Decrease the timer by 1 each time

# Printing final message
print("blast off!")

