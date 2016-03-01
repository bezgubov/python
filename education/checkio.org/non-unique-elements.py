#!/usr/bin/python

# data = [1, 2, 3, 4, 5]
data = [10, 9, 10, 10, 9, 8]
new_data = []

for element in data:
    if data.count(element) > 1:
        new_data.append(element)

data = new_data
print data
