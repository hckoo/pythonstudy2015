import os
import sys
import time
import datetime
import shutil

#filePath = "D:\\"
#targetPath = "C:\\temp\\"
 
def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        #print('Error: %s' % e)
        pass
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror) 


def elapsedTime(modifiedTime):
	#print  datetime.datetime.fromtimestamp(time.time())
	return time.time() - modifiedTime;

def main(filePath,targetPath):
	for (path, dir, files) in os.walk(filePath): 
	    for filename in files:
	        ext = os.path.splitext(filename)[-1] 
	        if ext == '.py': 
	        	filename = os.path.join(path, filename);
	        	modifiedTime = os.path.getmtime(filename)
	        	print("%s/%s//%s" % (path, filename,datetime.datetime.fromtimestamp(modifiedTime)))
	        	
	        	if elapsedTime(modifiedTime) < 120.0:
	        		copyFile(filename, targetPath)
	        		print "SUCCES EVENT"

if __name__ == '__main__':
	
	if(len(sys.argv) is 1):
		print ("input parameter please..")
		sys.exit(0)
	# if(len(sys.argv) < 2):
	# 	print ("input path parameter please..")
	# if(len(sys.argv) < 3):
	# 	print ("input targetPath parameter please..")
	
	main(sys.argv[1],sys.argv[2])
#print time.time()        	