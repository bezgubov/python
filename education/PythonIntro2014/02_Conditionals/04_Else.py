#!/usr/bin/env python


def get_data():
    circle = input("x,y,r: ")

    if type(circle) != tuple or len(circle) != 3:
        print "You wrong"
        quit()

    coordinates = input("x1,y1,x2,y2...xn,yn: ")

    if type(coordinates) != tuple or len(coordinates) % 2 != 0:
        print "You wrong"
        quit()

    return circle, coordinates


def check_dots(circle, coordinates):

    c_x = circle[0]
    c_y = circle[1]
    c_r = circle[2]

    dots = list(coordinates)

    answers = []

    while dots:
        dot_x = dots.pop(0)
        dot_y = dots.pop(0)
        c_x_range = range(c_x - c_r, c_x + c_r + 1)
        c_y_range = range(c_y - c_r, c_y + c_r + 1)
        if dot_x in c_x_range and dot_y in c_y_range:
            answers.append('YES')
        else:
            answers.append('NO')
    if 'NO' in answers:
        print 'NO'
    else:
        print 'YES'


def main():
    circle, coordinates = get_data()
    check_dots(circle, coordinates)

if __name__ == "__main__":
    main()
