import os.path, time
import easygui

def renameVideo(path):
    dir_time = time.localtime(os.stat(path).st_ctime)
    dirtime = time.strftime('%Y-%m%d', dir_time)                   #文件夹的路径
    msg = '文件的创建时间是{}吗？'.format(dirtime)
    choice = easygui.boolbox(msg,choices=('Yes', 'No'))
    if choice == 1:
        cTime = dirtime
    else :
        cTime = input('请输入文件的创建时间"2021-0221"\n')
    someone = input('请输入"人物"\n')
    someone.strip()
    place = input('请输入"地点"\n')
    place.strip()
    doing = input('请输入"活动"\n')
    doing.strip()
    filelist = os.listdir(path)
    filelist.sort(key=lambda x: os.path.getmtime(os.path.join(path, x)))
    for xh in range(1,len(filelist)+1):
        filename = filelist[xh-1]
        xh = '%03d' % xh
        oldfname = os.path.join(path,filename)
        # createdTime = time.localtime(os.stat(oldfname).st_mtime)
        # cTime = time.strftime('%Y-%m%d', createdTime)
        file_suffix = os.path.splitext(filename)[-1]
        newname  = '-'.join([cTime,someone,place,doing,xh]) + file_suffix
        newfname = os.path.join(path,newname)
        os.rename(oldfname,newfname)

def main():
    msg = '请点选要批量更名的video所在文件夹'
    print(msg)
    path = easygui.diropenbox(msg)
    # path = r'G:\新建文件夹\20210221VS黎老师于五楼'
    renameVideo(path)

if __name__=='__main__':
    main()
