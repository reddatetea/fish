import time
import os

fname = r'F:\a00nutstore\fishc\addqita.py'
path,filename = os.path.split(fname)

os.chdir(path)

file_times_create = time.localtime(os.path.getctime(fname))
print('文件属性最近修改的时间(ctime):  ',file_times_create)