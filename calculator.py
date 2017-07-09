
def input_number(message):
    x = raw_input(message)
    while not x.isdigit():
        print('it is not a number')
        x = raw_input(message)
    return int(x)


def main():
    print("Hello! Welcome to VCalculator 2.0!")
    stop = False
    while not stop:
        x = input_number("Enter first number:")
        y = input_number("Enter second number:")

        operator = raw_input("Enter operator [+, -, x (multiplication), % (division), ? (comparison):")
        if operator == '+':
            print("{}".format(x + y))
        elif operator == "-":
            print("{}".format(x - y))
        elif operator == 'x':
            print("{}".format(x * y))
        elif operator == '%':
            if y != 0:
                print("{}".format(float(x) / y))
            else:
                print('cannot divide by zero!')
        elif operator == '?':
            if x < y:
                print('{} < {}'.format(x, y))
            elif x > y:
                print('{} > {}'.format(x, y))
            else:
                print('{} = {}'.format(x, y))
        else:
            print('unknown operator!')
        response = raw_input("Do you want to continue? [y/n]")
        if response == 'n' or response == 'N':
            stop = True


if __name__ == "__main__":
    main()
