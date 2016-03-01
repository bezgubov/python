#!/usr/bin/python

phrases = ('Hello World!',
           'How do you do?',
           'One',
           'Oops!',
           'AAaoOoo!!!!',
           '9999990000000h',
           'fsbd')


def checkio(text):

    import re

    no_lit = '[ \-!?.,@;:\"\'=+_0123456789]'
    text = re.sub(no_lit, '', text).lower()

    letter_dict = {}

    for letter in text:
        try:
            if letter_dict[letter]:
                letter_dict[letter] += 1
        except:
            letter_dict[letter] = 1

    digit_max = max(letter_dict, key=letter_dict.get)
    letter_max = min(letter_dict.keys())

    if digit_max == letter_max:
        return digit_max
    elif digit_max != letter_max:
        if letter_dict.get(digit_max) > letter_dict.get(letter_max):
            return digit_max
        elif letter_dict.get(digit_max) == letter_dict.get(letter_max):
            letter_dict.pop(digit_max)
            return letter_max


def main():
    for phrase in phrases:
        print checkio(phrase)

if __name__ == "__main__":
    main()
