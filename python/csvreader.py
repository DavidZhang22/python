import csv
import os

empty = []
data = [8186,8282,8558,8770,8917,9146,9351]

with open('daily_total_cases.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in data:
    	writer.writerow([i])

'''print(os.scandir(r'/Users/David Zhang/Documents'))
with open(r'/Users/David Zhang/Downloads/data.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		empty.append(row)

new = []
for i in range(len(empty)):

	empty[i] = [empty[i][1], empty[i][3]]

	if empty[i][0] == "California":
		new.append(empty[i])

print(len(new))

with open('daily_total_cases.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in new:
    	writer.writerow(i)'''