#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import calculator_1

    args = sys.argv
    n = len(args) - 1

    if n != 3:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        if args[2] == '+':
            print("{} + {} = {:d}".format(args[1], args[3], calculator_1.add(int(args[1]), int(args[3]))))
        elif args[2] == '-':
            print("{} - {} = {:d}".format(args[1], args[3], calculator_1.sub(int(args[1]), int(args[3]))))
        elif args[2] == '*':
            print("{} * {} = {:d}".format(args[1], args[3], calculator_1.mul(int(args[1]), int(args[3]))))
        elif args[2] == '/':
            print("{} / {} = {:d}".format(args[1], args[3], calculator_1.div(int(args[1]), int(args[3]))))
        else:
            print(f"Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
