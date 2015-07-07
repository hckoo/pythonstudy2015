import os
import time

print(os.getcwd())
#metadata = os.stat('/Users/koo/python27/hello.py')
mtime = os.stat('hello.py').st_mtime
print(mtime)

print time.localtime(mtime)

import datetime
ctime = datetime.datetime.fromtimestamp(mtime)

print (ctime)

def modification_date(filename):
	t = os.path.getmtime(filename)
	return datetime.datetime.fromtimestamp(t)

d = modification_date('search_dir.py')
print d


current_time = time.time();
print current_time


