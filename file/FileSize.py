import os
import math


def inMB(fileName):
	size = round(os.path.getsize(fileName) / (1024 * 1024),2)
	return "{} MB".format(size) 
def inKB(fileName):
	size = round(os.path.getsize(fileName) / (1024),2)
	return "{} KB".format(size)
def inB(fileName):
	size = round(os.path.getsize(fileName),2)
	return "{} B".format(size)
