import xlrd 
import threading
from info.university.CampusAction import getDataFromUrl,getDataFromFile
from info.university.CampusType import CampusType
from file.excel.HeaderInfo import HeaderColumn




# file xlxs 
xlsFile 	= "this_is_file_excel.xlsx" 


# To open Workbook 
wb			= xlrd.open_workbook(xlsFile) 
sheet		= wb.sheet_by_index(0) 
numberofrow = sheet.nrows
 
 
threads = []  
for i in range(sheet.nrows): 
#skip the header
	if i==0: 
		continue
	number 		= sheet.cell_value(i, HeaderColumn.NUMBER)
	campusName 	= sheet.cell_value(i, HeaderColumn.CAMPUS_NAME)
	majorUrl 	= sheet.cell_value(i, HeaderColumn.MAJOR_URL)
	minorUrl 	= sheet.cell_value(i, HeaderColumn.MINOR_URL)
	majorTag 	= sheet.cell_value(i, HeaderColumn.MAJOR_TAG)
	minorTag 	= sheet.cell_value(i, HeaderColumn.MINOR_TAG)
	
	print("====================================") 
	print("Indexing : {number:02d}".format(number=int(number))) 
	print("Hit to url : \nMajor : {}\nMinor : {}".format(majorUrl,minorUrl))    
	
	if majorTag in "filetext":
		t1 = threading.Thread(target = getDataFromFile,args = (i,campusName,CampusType.MAJOR))
		t1.start()
		threads.append(t1)
	elif majorTag != "invalidurl" and  majorTag != "json" :
		t2 = threading.Thread(target = getDataFromUrl,args = (i,campusName,majorUrl,majorTag,CampusType.MAJOR))
		t2.start()
		threads.append(t2)
	if minorTag in "filetext":
		t3 = threading.Thread(target = getDataFromFile,args = (i,campusName,CampusType.MINOR))
		t3.start()
		threads.append(t3)
	elif majorTag != "invalidurl" and  majorTag != "json" :
		t4 = threading.Thread(target = getDataFromUrl,args = (i,campusName,majorUrl,majorTag,CampusType.MINOR))
		t4.start()
		threads.append(t4)
	print("====================================\n")    



for thread in threads:
	thread.join()
print("=================DONE==============\n")    
