import time 
import os

source = ['/home/zee/spider/','/home/zee/static/']
target_dir = '/home/zee/python_learning/Python_learning/day_03/back_up/'

today = target_dir+time.strftime('%Y-%m-%d')
print today

now = time.strftime('%H:%M:%S')

if not os.path.exists(today):
	os.mkdir(today)
	print 'successfully created  directory'

print os.sep
# os.sep /

target = today+os.sep+'.zip'

zip_command = "zip -qr '%s' %s" %(target,' '.join(source))

if os.system(zip_command) == 0:
	print 'successfully back up to',target
else:
	print 'backup failed'