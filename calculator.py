def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    if 0 is x or y:
        print("Invalid value for denominator, can't divide by 0!")
    else:
        return x / y


def multiply(x, y):
    return x * y


def square(x):
    return x * x


def power(x, y):
    return x * (y * x)


def sqrt(x):
    x / x
