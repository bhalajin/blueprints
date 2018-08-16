import csv

a = [[1,2,3], [4,5,6]]

with open('test.csv', 'w', newline='') as testfile:
	csvwriter = csv.writer(testfile)
	for row in a:
		csvwriter.writerow(row)

with open('test.csv', 'r') as testfile:
	csvreader = csv.reader(testfile)
	for row in csvreader:
		print(row)