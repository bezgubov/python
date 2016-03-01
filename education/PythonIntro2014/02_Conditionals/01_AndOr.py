#!/usr/bin/env python


def input_ab():
    a = input("1 = ")
    b = input("2 = ")
    return a, b

def compare(a,b):
     if a or b:
         print a or b
     else:
         print 'NO'

def main():
    a, b = input_ab()
    compare(a,b)

if __name__ == '__main__':
    main()
