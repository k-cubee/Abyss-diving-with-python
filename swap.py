print("\033c")
value1 = input("Enter first number: ")
value2 = input("Enter second number: ")
if value1 > value2:
    temp = value2
    value2 = value1
    value1 = temp
print(value1, value2)
print(temp)
