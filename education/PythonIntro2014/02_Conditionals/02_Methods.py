#!/usr/bin/env python


def main():
    obj = input("obj = ")
    for m in dir(obj):
        if m[0] != '_':
            print m

if __name__ == '__main__':
    main()
