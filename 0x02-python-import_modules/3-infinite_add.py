#!/usr/bin/python3

if __name__ == "__main__":
    import sys

result = 0
count = len(sys.argv)

if count == 1:
    result = 0
else:
    for i in range(1, count):
        result = result + int(sys.argv[i])
        print("{}".format(result))
