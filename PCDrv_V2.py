import os
import ConfigParser
import pypyodbc
import time
import datetime
import codecs
from ctypes import *
from time import localtime, strftime



libc = windll.LoadLibrary("D:\\SQMS\\DLApi.dll")

def readScreenPrinter(_file,_dir):

	config = ConfigParser.ConfigParser()
	config.read(_file)

	# data.append(config.get('PRESS_INFO','PRESSURE_FRONT'))
	# data.append(config.get('PRESS_INFO','PRESSURE_REAR'))

	libc.DLSetTagDataByName
	libc.DLSetTagDataByName.argtypes = [c_char_p,c_float]
	libc.DLSetTagDataByName.restype = c_bool

	cf_p = c_char_p('%s_FPRPV' % _dir)
	cf_f = c_float(float(config.get('PRESS_INFO','PRESSURE_FRONT')))
	libc.DLSetTagDataByName(cf_p,cf_f)
	
	cr_p = c_char_p('%s_RPRPV' % _dir)
	cr_f = c_float(float(config.get('PRESS_INFO','PRESSURE_REAR')))
	libc.DLSetTagDataByName(cr_p,cr_f)

def readFileSplit(_file):
	data =[]
	logFile = open(_file).read().splitlines()
	for line in logFile:
		data.append(line.replace('\0',''))

	# print data[len(data)-2]
	return (data[len(data)-2]).split('\t')

def readFileCodecs(_file):

	logFile =  codecs.open( _file, "r", "utf-8",errors='ignore')
	line = logFile.read().replace('\0','').strip().split('\n')

	return (line[len(line)-1]).split('\t')


def setDataIndex1(_data,_dir):

	libc.DLSetTagDataByName
	libc.DLSetTagDataByName.argtypes = [c_char_p,c_float]
	libc.DLSetTagDataByName.restype = c_bool

	UTMPV = [2,6,10,14,18,22,26,30,34,38]
	DTMPV = [4,8,12,16,20,24,28,32,36,40]

	for i in range(1,10):
		libc.DLSetTagDataByName(c_char_p('%s_UTMPV%d' % (_dir,i)),c_float(float(_data[UTMPV[i-1]])))
		libc.DLSetTagDataByName(c_char_p('%s_DTMPV%d' % (_dir,i)),c_float(float(_data[DTMPV[i-1]])))


def setDataIndex2(_data,_dir):

	libc.DLSetTagDataByName
	libc.DLSetTagDataByName.argtypes = [c_char_p,c_float]
	libc.DLSetTagDataByName.restype = c_bool


	UTMPV = [3,9 ,15,21,27,33,39,45,51,57]
	DTMPV = [6,12,18,24,30,36,42,48,54,60]

	for i in range(1,10):
		libc.DLSetTagDataByName(c_char_p('%s_UTMPV%d' % (_dir,i)),c_float(float(_data[UTMPV[i-1]])))
		libc.DLSetTagDataByName(c_char_p('%s_DTMPV%d' % (_dir,i)),c_float(float(_data[DTMPV[i-1]])))

def readReflow(_file,_dir):

	if _dir == 'R_02':
		setDataIndex1(readFileCodecs(_file),_dir)
	elif _dir == 'R_05':
		setDataIndex2(readFileSplit(_file),_dir)

def readICT(_file,_dir):
	data =[]
	logFile = open(_file,"r").readlines()
	for line in logFile:
		if line.find(':') > 0:
			thisLine = line.split(':')
			if 'PCB Name' == (thisLine[0]).strip():
				data.append(_dir)
				data.append(thisLine[1].replace('\n', ''))
			elif 'Test Time' == (thisLine[0]).strip():
				data.append(thisLine[1]+":"+thisLine[2]+":"+thisLine[3].replace('\n',''))	
				data.append('')
				data.append('')

	connect = pypyodbc.connect('DSN=SQMS1;PWD=tbsqms123;UID=sq_manager')
	cursor = connect.cursor()

	cursor.execute("insert into monitoring_ict(facil_tag_nm,item_cd,inspect_dt,ok_ng,create_dt) values ( ?,?,?,?,? )",data)
	cursor.commit()
	connect.close()


def readAOI(_file,_dir):
	data =[]
	logFile = open(_file,"r").readlines()
	thisLine = logFile[0].split(";")
	
	data.append(_dir)
	data.append(thisLine[0])
	data.append(thisLine[6]+thisLine[7])
	data.append(thisLine[4])

	connect = pypyodbc.connect('DSN=SQMS1;PWD=tbsqms123;UID=sq_manager')
	cursor = connect.cursor()

	cursor.execute("insert into monitoring_aoi(facil_tag_nm,item_cd,error_dt,error_nm) values ( ?,?,?,? )",data)
	cursor.commit()
	connect.close()

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
			if dir.startswith('SP_'):
				if elapsedTime(modifiedTime) is True:
					readScreenPrinter(fullPath,dir)
			elif dir.startswith('R_'):
				if file.find('data') > 0:
					if elapsedTime(modifiedTime) is True:
						readReflow(fullPath,dir)
			elif dir.startswith('AO_'):
				if elapsedTime(modifiedTime) is True:
					readAOI(fullPath,dir)
			elif dir.startswith('IC_'):
				if elapsedTime(modifiedTime) is True:
					readICT(fullPath,dir)


if __name__ == '__main__':
	while True:
		print "[%s] PCDrv_V2.exe START" % strftime("%y/%m/%d %H:%M:%S", localtime())   
		search()
		time.sleep(10)