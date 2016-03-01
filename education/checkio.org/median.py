#!/usr/bin/python

# data = [3, 4, 9, 6, 7, 8]
data = [1, 1, 1, 1, 3, 6, 20, 99, 10, 15]

data_len = len(data)
center = data_len // 2
sort_data = sorted(data)

if data_len % 2 == 1:
    data[0] = sort_data[data_len // 2]
else:
    left_center = sort_data[center]
    right_center = sort_data[center - 1]
    data[0] = (float(left_center) + float(right_center)) / 2

print data[0]
