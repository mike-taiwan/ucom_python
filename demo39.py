#encoding=UTF-8
import os
print os.getcwd()
dir1 = 'hello'
os.mkdir(dir1)
os.chdir(dir1)
print os.getcwd()
os.chdir('..')
os.rmdir(dir1)
dir2 = u'資料'
os.mkdir(dir2)
os.chdir(dir2)
print os.getcwd().decode('ms950')
os.chdir('..')
os.rmdir(dir2)

import sys

print sys.executable
print sys.argv