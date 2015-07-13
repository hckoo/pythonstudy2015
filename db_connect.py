import os
import ConfigParser
import pypyodbc

import pickle

def readICT(_file):
	data =[]
	#  line = line.replace("\n", "");
	logFile = open(_file,"r").readlines()
	for line in logFile:
		if line.find(':') > 0:
			thisLine = line.split(':')
			if 'PCB Name' == (thisLine[0]).strip():
				data.append(thisLine[1])
			elif 'Test Time' == (thisLine[0]).strip():
				data.append(thisLine[1]+":"+thisLine[2]+":"+thisLine[3])	

	return data

def readAOI(_file):
	data =[]
	logFile = open(_file,"r").readlines()
	thisLine = logFile[0].split(";")
	
	data.append(thisLine[0])
	data.append(thisLine[6]+thisLine[7])
	data.append(thisLine[4])

	return data

def readScreenPrinter(_file):
	data =[]
	config = ConfigParser.ConfigParser()
	config.read(_file)

	data.append(config.get('PRESS_INFO','PRESSURE_FRONT'))
	data.append(config.get('PRESS_INFO','PRESSURE_REAR'))
	return data

def readReflow(_file,_dir):
	# rfData =[]
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


	

	# if _dir == "R_02":
		# fileObj = codecs.open( _file, "r", "utf-8" )
		# logFile = fileObj.readlines()
		# print _dir
		# print _file
		# logFile = open(_file,"r").readlines()
		# print len(logFile)
		# print logFile[len(logFile)-1]
		# print logFile[-1]
		# print os.stat(_file)

		# print open(_file,'r').read().count('\n')
		# with open(_file) as ifp:
		    # for line in ifp:
		    #     print line
	# return rfData 

pwd = "D:\\SQMS\\Recv"
for path, dirs, files in os.walk(pwd):
	dir = path.split("\\")[-1]
	
	if dir == pwd.split("\\")[-1]:
		continue

	# print dir
	for file in files:
		fullPath = path+"\\"+file
		#print os.path.dirname(file)
		# print os.path.splitext(file)
		# if dir.startswith('SP_'):
		# 	# print readScreenPrinter(fullPath)

		if dir.startswith('R_'):
			if file.find('data') > 0:
				# print dir
				readReflow(fullPath,dir)
		# elif dir.startswith('AO_'):
		# 	# print readAOI(fullPath)
		# elif dir.startswith('IC_'):
		# 	# print readICT(fullPath)	
		# else:
			# print file



# connect = pypyodbc.connect('DSN=SQMS1;PWD=tbsqms123;UID=vs_manager')
# cursor = connect.cursor() 

# rows = []
# row = ['TEST11', 'ITEM_CD','20150710','OK','']
# for i in range(len(row)):
#     rows.append(row)

# cursor.execute("insert into monitoring_ict(facil_tag_nm,item_cd,inspect_dt,ok_ng,create_dt) values ( ?,?,?,?,? )",row)
# cursor.commit()
