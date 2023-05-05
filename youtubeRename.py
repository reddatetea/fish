# coding = 'uft-8'
import re
import os

path = 'D:\\youtube\\abc'
os.chdir(path)
fileList = os.listdir(path)
#print(fileList)
for filename in fileList :
    #print(filename)
    regex = r'(_|-\s?\w*)*(?=\.mp4)'
    pattern = re.compile(regex)
    newname = pattern.sub('',filename)
    print(newname)
    os.rename(filename,newname)