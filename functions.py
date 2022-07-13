print("\033c")
x = 1+1
y = 2+2


def printNumber(number):
    print(number)
    return number + 2


print(printNumber(x))


def nameAndAge(name, age):
    print("Hi! You are " + name + " and you are " + str(age) + " years old!")


nameAndAge("James", 20)
