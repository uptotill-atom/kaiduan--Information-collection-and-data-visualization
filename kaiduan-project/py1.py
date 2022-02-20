import csv

from pyecharts import options as opts
from sympy.combinatorics import Subset

with open('data.csv') as csvFile:
    reader = csv.reader(csvFile)

    data1 = [str(row[0]) for row in reader]

    #print(data1)
print(type(data1))

set_seq = set(data1)
rst = []
for item in set_seq:
    rst.append((item,data1.count(item)))
rst.sort()
print(type(rst))
print(rst)

with open('time1.csv', 'w+', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',')
    for i in rst:
        writer.writerow(i)

with open('time1.csv') as csvFile:
    reader = csv.reader(csvFile)
    x = [str(row[0]) for row in reader]
    print(x)

with open('time1.csv') as csvFile:
    reader = csv.reader(csvFile)
    y1 = [str(row[1]) for row in reader]
    print(y1)