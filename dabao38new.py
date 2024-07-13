'''
家中电脑，python311打包脚本。通过点选将要打包的程序、图标，生成完整的打包命令，自动粘贴到剪贴板上
'''

import os
import shutil
import pyperclip
import easygui


py_lst = ['bs4','docx','easygui','matplotlib','numpy','openpyxl','pandas','pdfplumber','pyperclip','xlwings','xpinyin','yagmail']
py_used = easygui.multchoicebox(msg='请选择要打包脚本中使用的库',title = '可多选',choices=py_lst)    #3.10版本必须有title
paichus = list(set(py_lst) - set(py_used))
paichu = ' '.join(['--exclude-module='+j for j in paichus])    #排除的库
dabao_pyinstall = r"D:\python38\Scripts\pyinstaller.exe"
ico = easygui.fileopenbox(msg='请点选ico图标文件')
path, file = os.path.split(ico)
os.chdir(path)
pyfile = easygui.fileopenbox(msg='请点选要打包的py文件')
file_way = r'-F -w -i'
tmpdir_way = r'--runtime-tmpdir=..'

#复制upx文件夹至要打包脚本所在文件夹
source_path = r'D:\a00nutstore\yingyongchengxu\upx-3.96-win64'
target_path = os.path.join(path,os.path.split(source_path)[-1])
if not os.path.exists(target_path):
    # 如果目标路径不存在原文件夹的话就创建
    os.makedirs(target_path)
if os.path.exists(source_path):
    # 如果目标路径存在原文件夹的话就先删除
    shutil.rmtree(target_path)
shutil.copytree(source_path, target_path)

upx_way = ''.join(['--upx-dir=',target_path])  #不能有空格''
daobao_lst = [dabao_pyinstall,upx_way,paichu,file_way,ico,tmpdir_way,pyfile]
daobao_commond = ' '.join(daobao_lst)   #有一个空格''
pyperclip.copy(daobao_commond)
easygui.msgbox(msg='程序结束，请cmd到命令行模式 粘贴后 运行')


