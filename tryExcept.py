import turtle
from unittest import result


print("\033c")
try:
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisior: "))
    result = dividend / divisor
    print(result)
except ValueError:
    print("Invalid input")
except ZeroDivisionError as err:
    print(err)
