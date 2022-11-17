def main():
    calculate()


def calculate():
    num1 = float(input("Enter the first number: "))
    op = input("Enter the operator: ")
    num2 = float(input("Enter the second number: "))

    if op == "+":
        print(f"result = {num1 + num2}")
    elif op == "-":
        print(f"result = {num1 - num2}")
    elif op == "/":
        print(f"result = {num1 / num2}")
    elif op == "*":
        print(f"result = {num1 * num2}")
    else:
        print("Invaild operator")

    while True:
        calculate_again = input("Do you want to perform another calculation: ")
        if calculate_again.upper() == "YES":
            calculate()
        else:
            break
