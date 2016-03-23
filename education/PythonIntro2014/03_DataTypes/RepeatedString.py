#!/usr/bin/env python


def check_string(s, t):
    if len(s) % len(t) == 0 or s == t:
        check = t * (len(s) / len(t))
        if check == s or len(check) < len(s):
            return len(s) / len(t)


def main():
    s = str(raw_input())
    k = []
    t = ''

    for l in s:
        t += l
        k.append(check_string(s, t))

    print max(k)

if __name__ == "__main__":
    main()
