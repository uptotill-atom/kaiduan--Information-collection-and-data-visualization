import csv

csvFile = open("content.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open('content.txt', 'r', encoding='utf-8')
for line in f:
    csvRow =line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()