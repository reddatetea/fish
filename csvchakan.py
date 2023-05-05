import os
import easygui
from csv import reader,writer

msg = '请点选要查看的csv文件'
title = 'csv文件'
fname = easygui.fileopenbox(msg,title)
path, filename = os.path.split(fname)
os.chdir(path)
inputFile = open(filename, 'r',encoding = 'UTF-8')
csvReader = reader(inputFile)
for row in csvReader :
    #print(row)
    print(row[0])

inputFile.close()

