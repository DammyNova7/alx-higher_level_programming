#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    args = sys.argv
    n = len(args) - 1

    if n != 3:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(args[1])
        b = int(args[3])

        if args[2] == '+':
            print("{} + {} = {:d}".format(a, b, add(a, b)))
        elif args[2] == '-':
            print("{} - {} = {:d}".format(a, b, sub(a, b)))
        elif args[2] == '*':
            print("{} * {} = {:d}".format(a, b, mul(a, b)))
        elif args[2] == '/':
            print("{} / {} = {:d}".format(a, b, div(a, b)))
        else:
            print(f"Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
