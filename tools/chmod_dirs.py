#!/usr/bin/env python
import os
import sys

path = sys.argv[1]

if sys.argv == 3:
    mode = int(sys.argv[2], 8)
else:
    mode = int('0755', 8)


def tree(path, mode):
    path = path + '/'

    dirs = filter(lambda filename:
                  os.path.isdir(path + filename),
                  os.listdir(path))

    map(lambda dir: os.chmod(path + dir, mode), dirs)
    map(lambda dir: tree(path + dir, mode), dirs)

if __name__ == '__main__':
    tree(path, mode)
