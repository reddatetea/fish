import os
import time
#前缀1   名字
name = '堂堂'

#前缀2    地点
place = ''

#前缀3    方式
#文伟手机
way = 'wwsj'

#序列号
xlh = ''

#list1 =[]
#filePath = 'C:\\Users\\asus\\2015年06月'
filePath= input('请输入想要批量更名的完整路径:').strip()  #由用户指定文件路径，去除输入字符串前后空格
def totalRename(filePath):
    sortFile(filePath)
    renameFile(filePath)
    zcpl(filePath)

def sortFile(filePath):
    dir_list = os.listdir(filePath)
    fileList = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(filePath, x)))
    return fileList

def renameFile(filePath):
    fileList = sortFile(filePath)
    print(fileList)
    #print(fileList)
    for filename in fileList:
        for i in range(len(fileList)):
            xlh = '%03d'%(i+1)
            print(xlh)
            filename = fileList[i]
            print(filename)
            oldname = os.path.join(filePath,fileList[i])

            #statinfo=os.stat(os.path.join(filePath,filename))
            statinfo=os.stat(os.path.join(filePath,fileList[i]))


            createTimeStrimng = time.strftime('%Y%m%d%H%M%S',time.localtime(statinfo.st_mtime))

            abc = name+createTimeStrimng+place+way+xlh+ os.path.splitext(filename)[-1]
            #print(abc)
            newname = os.path.join(filePath,abc)
            os.chdir(filePath)
            os.rename(oldname,newname)

#文件夹更名后再次遍历，这次只针对文件夹
def zcpl(filePath):
    time.sleep(5)
    #nonlocal fileList
    fileList = sortFile(filePath)
    #print(fileList)
    for filename in fileList:
        #print(filename)
        pathTmp = os.path.join(filePath, filename)  # 获取path与filename组合后的路径
        #print(pathTmp)
        if os.path.isdir(pathTmp):  # 判断是否为目录
            totalRename(pathTmp)  # 是目录就继续递归查找
            #sortFile(pathTmp)
        elif os.path.isfile(pathTmp):
            pass

    return




#renameFile(filePath)
totalRename(filePath)



