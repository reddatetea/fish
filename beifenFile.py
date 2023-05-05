import os
import shutil
import datetime

def beifen(fname,beifen_dir=r'F:\a00nutstore\006\zw\beifen'):
    dqrq = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
    path,filename=os.path.split(fname)  #分解为路径和文件名
    qian,hou = os.path.splitext(filename)  #将文件名分解为前缀，后缀
    beifen_name = qian+'_'+dqrq + hou
    beifen_fname = os.path.join(beifen_dir,beifen_name)
    shutil.copyfile(fname,beifen_fname)

def main():
    fname = r'f:\a00nutstore\006\zw\else\2020入库.xlsx'
    beifen(fname,beifen_dir=r'F:\a00nutstore\006\zw\beifen')


if __name__ == '__main__':
    main()
