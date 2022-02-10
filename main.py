def main():
    while True:
        a = float(input('Input a: '))
        b = float(input('Input b: '))
        c = float(input('Input c: '))
        x_start = int(input('Input the start value of x: '))
        x_end = int(input('Input the end value of x: '))
        dx = int(input('Input dx: '))

        try:
            validate_all_numeric(a, b, c, x_start, x_end, dx)
            validate_range(x_start, x_end)
        except ValueError as ve:
            print(ve)

        header = ['x', 'f(x)']
        print("{:>20} {:>20}".format(*header))

        x = x_start
        while x <= x_end:
            try:
                f_value = f(a, b, c, x)
                row = [x, f_value]
                print("{:>20} {:>20}".format(*row))
                x += dx
            except ValueError as ve:
                print('Invalid params, try new ones')
                print(ve)
                break

        message = input('success! wanna quit? press q: ')
        if message == 'q':
            break


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
    return result


def validate_first_case(a, b, x):
    if 10 + b == 0:
        raise ArithmeticError('First case is invalid')


def validate_second_case(a, c, x):
    if x - c == 0:
        raise ArithmeticError('Second case is invalid')


def validate_third_case(x, c):
    if c == 0:
        raise ArithmeticError('Third case is invalid')


def validate_all_numeric(*argv):
    for val in argv:
        try:
            float(val)
        except ValueError:
            raise ValueError('Value ' + str(val) +
                             ' cannot be converted to numeric format')


def validate_range(start, end):
    if float(start) > float(end):
        raise ValueError('start value should be less than or equal than end value',
                         'start=' + str(start),
                         'end' + str(end))


if __name__ == '__main__':
    main()