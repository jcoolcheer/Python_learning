import os
import time
import calendar
print (time.time())
# 1488463306.43

print (time.localtime(time.time()))
# time.struct_time(tm_year=2017, tm_mon=3, tm_mday=2, tm_hour=22, tm_min=1, tm_sec=46, tm_wday=3, tm_yday=61, tm_isdst=0)

print (time.asctime(time.localtime(time.time())))
# Thu Mar 2 22:08:36 2017

print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
# 2017-03-02 22:08:36

print calendar.month(2017,3)
# output calendar

# --------------------about time in Python ---------------------------

source = ['/home/zee/spider/','/home/zee/static/']
target_dir = '/home/zee/python_learning/Python_learning/day_03/back_up/'
target = target_dir+time.strftime('%Y-%m-%d %H:%M:%S')+ '.zip'
print (time.strftime('%y%m%d%H%M%S'))

zip_command = "zip -qr %s %s"%(target, ' '.join(source))

print(zip_command)

if os.system(zip_command) == 0:
    print 'success!'
else:
	print 'error'
