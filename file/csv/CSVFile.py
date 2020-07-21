import csv

def write(datas,fileName):
	with open(fileName, 'w', newline='') as csvfile:
		csvwriter = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
		
		for data in datas:
			#print("writing {s}".format(s=data))
			csvwriter.writerow([data])
