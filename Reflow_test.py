#coding: utf-8

import os
import sys
import ConfigParser
import pypyodbc
from ctypes import *
import time
import datetime
from time import localtime, strftime
import codecs


reload(sys)
sys.setdefaultencoding('utf-8')

libc = windll.LoadLibrary("D:\\SQMS\\DLApi.dll")


def readFileSplit(_file):

	logFile = open(_file).read().splitlines()
	for line in logFile:
		data.append(line.replace('\0',''))
	return data[len(data)-1]

def readFileCodecs(_file):
	f =  codecs.open( _file, "r", "utf-8",errors='ignore')
	line = f.read().replace('\0','').strip().split('\n')
	return line[len(line)-1]


def readReflow(_file,_dir):
	
	# R01 NG
	# R02 OK
	# R03 NG
	# R04 NG
	# R05 OK
	# R06 NG
	# R07 NG
	# R08 NG
	# R09 NG
	# R10 NG

	if _dir == 'R_02':
		data = readFileCodecs(_file)
		print data.split('\t')[0]

	elif _dir == 'R05':
		data = readFileSplit(_fiel)



    

def elapsedTime(modifiedTime):
    #print  datetime.datetime.fromtimestamp(time.time())
    return time.time() - modifiedTime < 60.0;

def search():
	pwd = "D:\\SQMS\\Recv"
	for path, dirs, files in os.walk(pwd):
		dir = path.split("\\")[-1]
		
		if dir == pwd.split("\\")[-1]:
			continue

		# print dir
		for file in files:
			fullPath = path+"\\"+file
			modifiedTime = os.path.getmtime(fullPath)
			#print os.path.dirname(file)
			# print os.path.splitext(file)
			if dir.startswith('R_02'):
				if file.find('data') > 0:
					print fullPath
					readReflow(fullPath,dir)
			

if __name__ == '__main__':
	# while True:
		print "[%s] Reflow START" % strftime("%y/%m/%d %H:%M:%S", localtime())   
		search()
		# time.sleep(60)