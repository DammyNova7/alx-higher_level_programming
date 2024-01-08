#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    n = len(sys.argv) - 1
    result = 0

    if n == 0:
        result = 0
    else:
        for i in range(n):
            if n == 1:
                result += int(sys.argv[i + 1])
            else:
                result += int(sys.argv[i + 1])
    print(result)
