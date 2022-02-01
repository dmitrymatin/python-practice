import this


def f(a, b, c, x):
    if x < 0 and b != 0 and validate_first_case(a, b, x):
        return a - (x / (10 + b))
    elif x > 0 and b == 0 and validate_second_case(a, c, x):
        return (x - a) / (x - c)
    elif validate_third_case(x, c):
        return 3 * x + (2 / c)

    return 'error'


def validate_first_case(a, b, x):
    if 10 + b == 0:
        return False

    return True


def validate_second_case(a, c, x):
    if x - c == 0:
        return False

    return True


def validate_third_case(x, c):
    if c == 0:
        return False

    return True
