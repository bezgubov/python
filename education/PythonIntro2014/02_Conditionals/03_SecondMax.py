#!/usr/bin/env python


def main():
    my_list = input("List :")

    if type(my_list) == tuple:
       my_list = list(my_list)
    elif type(my_list) == int:
        my_list = [my_list]
    elif type(my_list) != list:
        print 'Wrong format!'

    first_max = max(my_list) 
    while first_max in my_list:
        my_list.remove(first_max)
    
    if my_list:
        print max(my_list)
    else:
        print "NO"

if __name__ == '__main__':
    main()
