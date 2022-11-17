print("\033c")
value1 = input("Enter first number: ")
value2 = input("Enter second number: ")
temp = value2
if value1 > value2:
    value2 = value1
    value1 = temp
print(value1, value2)
print(temp)
