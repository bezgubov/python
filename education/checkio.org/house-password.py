#!/usr/bin/python
import re

passwords = ["A1213pokl",
             "bAse730onE4",
             "asasasasasasasaas",
             "QWERTYqwerty",
             "123456123456",
             "QwErTy911poqqqq"]


def check_passwd(password):
    check = False
    if len(password) >= 10:
        if re.search('[0-9]+', password):
            if re.search('[a-z]+', password):
                if re.search('[A-Z]+', password):
                    check = 'True'
    return password, check

for password in passwords:
    print check_passwd(password)
