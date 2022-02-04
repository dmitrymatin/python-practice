def main():
    while True:
        a = input('Input a: ')
        b = input('Input b: ')
        c = input('Input c: ')
        x_start = input('Input the start value of x: ')
        x_end = input('Input the end value of x: ')
        dx = input('Input dx: ')

        try:
            validate_all_numeric(a, b, c, x_start, x_end, dx)
            validate_range(x_start, x_end)
            
            print('{:>20} {:>20}'.format(['']))
            
            x = x_end
            while x <= x_end:
                print('{:>20} {:>20}'.format(*['x', 'f(x)']))
                print('{:>20} {:>20}'.format(*[x, f(a, b, c, x)]))
                x += dx
        except ValueError as ve:
            print()


def f(a, b, c, x):
    try:
        if x < 0 and b != 0:
            validate_first_case(a, b, x)
            result = a - (x / (10 + b))
        elif x > 0 and b == 0:
            validate_second_case(a, c, x)
            result = (x - a) / (x - c)

        validate_third_case(x, c)
        result = 3 * x + (2 / c)
    except ArithmeticError as ae:
        raise ValueError('Function cannot be calculated because of incorrect parameters') \
            .with_traceback(ae)


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


def validate_all_numeric(*argv):
    for val in argv:
        if not str(val).isnumeric():
            raise ValueError('Value ' + val +
                             ' cannot be converted to numeric format')


def validate_range(start, end):
    if float(start) > float(end):
        raise ValueError('start value should be less than or equal than end value', 
            'start=' + str(start),
            'end' + str(end))
