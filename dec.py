#Divider

import sys
try:
    print("Divider calculator")
    x = int(input("First number: "))
    y = int(input("Second number: "))
except ValueError:
    print("Not a number. Exiting system")
    sys.exit()

try:
    result = x / y
except ZeroDivisionError:
    print("Cannot Divise by 0. Exiting system")
    sys.exit()

print(f"{x} / {y} = {result}")