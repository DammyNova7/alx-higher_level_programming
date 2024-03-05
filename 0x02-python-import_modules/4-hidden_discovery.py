#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)

    exceptions = [i for i in names if not i.startswith('__')]
    for i in exceptions:
        print(i)
