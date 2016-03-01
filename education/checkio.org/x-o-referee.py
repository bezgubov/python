#!/usr/bin/python

checkio1 = ([
    "X.O",
    "XX.",
    "XOO"]) # == "X"
checkio2 = ([
    "OO.",
    "XOX",
    "XOX"]) # == "O"
checkio3 = ([
    "OOX",
    "XXO",
    "OXX"]) # == "D"

def checkio(game_result):
    print game_result

def main():
    for game_result in checkio1, checkio2, checkio3:
        checkio(game_result)

if __name__ == "__main__":
    main()
