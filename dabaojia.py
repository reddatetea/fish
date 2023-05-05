'''
公司电脑，通过点选将要打包的程序、图标，生成完整的打包命令，自动粘贴到剪贴板上
'''

import os
import pyperclip
import easygui

py_lst = ['bs4', 'docx', 'easygui', 'matplotlib', 'numpy', 'openpyxl', 'pandas', 'pdfplumber', 'pyperclip',
                  'xlwings', 'xpinyin', 'yagmail']

choice1 = easygui.buttonbox(msg='请选择打包的环境',choices=['python39','python34'])
if choice1 == 'python39':
    dabao_python = r'D:\anaconda\python.exe'
    dabao_pyinstall = r'D:\anaconda\Scripts\pyinstaller.exe'
    
    choice = easygui.boolbox(msg='是否要排除一些库', choices=['是Yes', '否No'])
    if choice == True:
        py_used = easygui.multchoicebox(msg='请选择要打包脚本中使用的库', title='可多选', choices=py_lst)  # 3.10版本必须有title
        paichus = list(set(py_lst) - set(py_used))
        paichu = ' '.join(['--exclude-module=' + j for j in paichus])  # 排除的库
    else:
        paichu = ''

else :
    dabao_python = r'D:\python34\python32.exe'
    dabao_pyinstall = r'D:\python34\Scripts\pyinstaller-3.5\pyinstaller.py'
    paichu = ''

ico = easygui.fileopenbox(msg='请点选ico图标文件')
path,file=os.path.split(ico)
os.chdir(path)
pyfile = easygui.fileopenbox(msg='请点选要打包的py文件')
file_way = r'-F -w -i'
tmpdir_way = r'--runtime-tmpdir=..'
daobao_lst = [dabao_python,dabao_pyinstall,paichu,file_way,ico,tmpdir_way,pyfile]
daobao_commond = ' '.join(daobao_lst)
pyperclip.copy(daobao_commond)
easygui.msgbox(msg='程序结束，请cmd到命令行模式，并cd进入到要打包脚本所在目录 粘贴后 运行')


