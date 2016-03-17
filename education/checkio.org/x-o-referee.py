#!/usr/bin/python

checkio1 = ([
    "X.O",
    "XX.",
    "XOO"])  # == "X"
checkio2 = ([
    "OO.",
    "XOX",
    "XOX"])  # == "O"
checkio3 = ([
    "OOX",
    "XXO",
    "OXX"])  # == "D"
checkio4 = ([
    "OOX",
    "XXO",
    "XXX"])  # == "D"
checkio5 = ([
    "OOO",
    "XXO",
    "XXX"])  # == "ERR"
checkio6 = ([
    "...",
    "...",
    "..."])  # == "D"
checkio7 = ([
    "O.X",
    "XX.",
    "XOO"])  # == "X"


def get_diag(game_result):
    result = []
    diag_1 = []
    diag_2 = []

    for xy in range(3):
        diag_1.append(game_result[xy][xy])

    y = 2
    for x in range(3):
        diag_2.append(game_result[x][y])
        y -= 1

    result.append(check_row(diag_1))
    result.append(check_row(diag_2))
    
    return result


def get_horiz(game_result):
    result = []

    for row in game_result:
        horiz = list(row)
        result.append(check_row(horiz))

    return result


def get_vert(game_result):
    result = []

    for x in range(3):
        vert = []
        for y in range(3):
            vert.append(game_result[y][x])
        result.append(check_row(vert))

    return result


def check_row(row):
    result = {"X": 0, "O": 0, ".": 0}
    win = []

    for i in row:
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1

    if result["X"] == 3:
        win.append("X")
    elif result["O"] == 3:
        win.append("O")
    else:
        win.append("D")

    if len(win) > 1:
        win[0] = 'ERR'

    return win[0]


def checkio(game_result):
    print 'game result'
    for line in game_result:
        print line

    result = []
    result.extend(get_diag(game_result))
    result.extend(get_horiz(game_result))
    result.extend(get_vert(game_result))

    if "X" in result and "O" in result:
        print "Wrong result!"
    elif "ERR" in result:
        print "Wrong result!"
    elif "X" in result:
        print "X"
    elif "O" in result:
        print "O"
    elif "X" or "O" or "ERR" not in result:
        print "D"
    else:
        print "Something wrong!"


def main():
    results = [checkio1,
               checkio2,
               checkio3,
               checkio4,
               checkio5,
               checkio6,
               checkio7]

    for game_result in results:
        checkio(game_result)

if __name__ == "__main__":
    main()
