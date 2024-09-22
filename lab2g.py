#!/usr/bin/env python3
import sys

# Author: Arshdeep Singh
# Author ID: aswalia6
# Date Created: 2024/09/21  

# Check if an argument is provided
if len(sys.argv) == 2:
    timer = int(sys.argv[1])  # Set timer to the command line argument
else:
    timer = 3  # Default timer value

# Loop until the timer reaches 0
while timer > 0:
    print(timer)
    timer -= 1  # Decrease the timer by 1 each time

# Print "blast off!" at end
print("blast off!")
