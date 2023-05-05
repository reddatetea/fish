#根据一个文件夹下全部是中文名文件，另外一个文件夹下全部是拼音名文件，本模块将拼音名文件全部更新为中文名！两个文件夹下的后缀可以不同下

import os
import easygui
from xpinyin import Pinyin
import shutil

def getpinyin(chinese_str):
    p = Pinyin()
    pinyins = p.get_pinyin(chinese_str, '-')
    name_pinyins = ' '.join([i.capitalize() for i in pinyins.split('-')] )
    return name_pinyins

def main():
    msg = '请点选已破解的azw文件夹'
    azw_path = easygui.diropenbox(msg)
    #azw_path = r'C:\Users\Administrator\AppData\Roaming\decrypt'
    azw_files = [file for file in os.listdir(azw_path) if file.split('.')[-1]=='azw3']
    azw_pinyins = [getpinyin(azw_file) for azw_file in  azw_files]
    msg = '请点选已转换为txt的"Calibre 书库"所在文件夹'
    #calibre_txt_path = r'G:\calibri书库'
    calibre_txt_path = easygui.diropenbox(msg)
    txt_files = [os.path.join(root,file) for root,dirs,files in os.walk(calibre_txt_path)  for file in files if file.split('.')[-1] == 'txt']
    print(txt_files)
    for txt_file in txt_files :
        for j in range(len(azw_pinyins)) :
            if azw_pinyins[j].startswith(os.path.split(txt_file)[1][:4]):             #前四个拼音如果相同，则判定两个文件名中文和拼音是对应的
                old_name = txt_file
                prefix,suffix = azw_files[j].split('.')
                filename = prefix +'.'+'txt'
                new_name = os.path.join(azw_path,filename)
                shutil.copyfile(old_name,new_name)      #why os.rename can't do this?

if __name__ == '__main__':
    main()