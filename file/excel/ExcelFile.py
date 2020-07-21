import csv



class CSV:

	def write(self,fileName):
		with open(fileName, 'w', newline='') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow(['1'])
			spamwriter.writerow(['2'])
			spamwriter.writerow(['3'])
