import requests 
import csv
import sys
import array as arr
import time
from bs4 import BeautifulSoup
from connection.ssl.SSLHelper import no_ssl_verification
from file.csv.CSVFile import write
from file.FileSize import inMB,inKB,inB
from info.university.CampusType import CampusType





def getDataFromUrl(index, campusName, url, tagSelector,campusType):
	with no_ssl_verification():
		try:
			headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
			resultMajor = requests.get(url.strip(),timeout=60,headers=headers)
		except OSError as err:
			print("=======================================")
			print("Url Connection Error.....")
			print("[{0}]".format(url))
			print("{0}".format(err))
			print("=======================================")
			time.sleep(5)
			return
			

		soup = BeautifulSoup(resultMajor.content,"html.parser")
		rows = soup.select(tagSelector)
		insertData = []
		for row in rows:
			insertData.append(row.get_text())
			
		outputFolder 	= "output";	
		if(campusType == CampusType.MAJOR):
			outputFileName 	= "{outputFolder}/{index:02d}.{fileName}_major.csv"
		elif(campusType == CampusType.MINOR):
			outputFileName 	= "{outputFolder}/{index:02d}.{fileName}_minor.csv"
		else:
			sys.exit()
		
		fileOutput = outputFileName.format(outputFolder=outputFolder,index=index,fileName=campusName.lower()).replace(" ","_")
		write(insertData,fileOutput)
		print("{i:02d}.File [{}] has a size {}".format(fileOutput,inKB(fileOutput),i=index))
		
def getDataFromFile(index, campusName, campusType):

	if(campusType == CampusType.MAJOR):
		fileType = "major"
	elif(campusType == CampusType.MINOR):
		fileType = "minor"
	else:
		sys.exit()
		
	inputFolder = "/home/sandy/Desktop/TMP/university_info/input" 
	inputFile 	= "{}/{index:02d}/{fileType}.txt".format(inputFolder,index=index,fileType=fileType)
	# Using readlines() 
	filetxt = open(inputFile, 'r') 
	lines = filetxt.readlines()
	insertData = []
	for line in lines: 
		line = line.strip()
		if line == "":
			continue
		if len(line) == 1:
			continue
		insertData.append(line)
		#print("{}".format(line))

	outputFolder 	= "output";	
	if(campusType == CampusType.MAJOR):
		outputFileName 	= "{outputFolder}/{index:02d}.{fileName}_major.csv"
	elif(campusType == CampusType.MINOR):
		outputFileName 	= "{outputFolder}/{index:02d}.{fileName}_minor.csv"
	else:
		sys.exit()
		
	fileOutput = outputFileName.format(outputFolder=outputFolder,index=index,fileName=campusName.lower()).replace(" ","_")
	write(insertData,fileOutput)
	print("{i:02d}.File [{}] has a size {}".format(fileOutput,inKB(fileOutput),i=index))



