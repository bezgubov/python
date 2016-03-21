#!/usr/bin/env python


def main():
    data = input()
    evens = []
    odds = []
    i = 0

    for obj in data:
        if i % 2 == 0:
            evens.append(obj)
        else:
            odds.append(obj)
        i += 1

    print tuple(evens[::-1] + odds)

if __name__ == '__main__':
    main()
