import csv
import time

csvFile = open("data.csv",'w',newline='',encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("time.txt",'r',encoding='utf-8')
for line in f:
    csvRow = int(line)

    timeArray = time.localtime(csvRow)
    csvRow = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(csvRow)
    csvRow = csvRow.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()
