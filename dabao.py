'''
家里和公司电脑通用，通过点选将要打包的程序、图标，生成完整的打包命令，自动粘贴到剪贴板上
'''

import os
import shutil
import pyperclip
import easygui

py_lst = ['bs4', 'docx','easygui', 'matplotlib', 'numpy', 'openpyxl', 'pandas', 'pdfplumber', 'pyperclip',
                  'xlwings', 'xpinyin', 'yagmail']

choice1 = easygui.buttonbox(msg='请选择打包的环境',choices=['python38','python34','python311'])
if choice1 == 'python38':
        dabao_python = r'D:\python38\Scripts\pyinstaller.exe'
        dabao_pyinstall = r''
elif choice1 == 'python311':
    dabao_python = r'D:\python311\Scripts\pyinstaller.exe'
    dabao_pyinstall = r''
else :
    dabao_python = r'D:\python34\python32.exe'
    dabao_pyinstall = r'D:\python34\Scripts\pyinstaller-3.5\pyinstaller.py'
    upx_way = ''

ico = easygui.fileopenbox(msg='请点选ico图标文件')
path,file=os.path.split(ico)
os.chdir(path)
pyfile = easygui.fileopenbox(msg='请点选要打包的py文件')
file_way = r'-F -w -i'
tmpdir_way = r'--runtime-tmpdir=..'
#复制upx文件夹至要打包脚本所在文件夹
source_path = r'F:\a00nutsrore\yingyongchengxu\upx-3.96-win64'
target_path = os.path.join(path,os.path.split(source_path)[-1])
if not os.path.exists(target_path):
    # 如果目标路径不存在原文件夹的话就创建
    os.makedirs(target_path)
if os.path.exists(source_path):
    # 如果目标路径存在原文件夹的话就先删除
    shutil.rmtree(target_path,)
shutil.copytree(source_path, target_path)
upx_way = ''.join(['--upx-dir=',target_path])  #不能有空格''

dll_exclus = ['vcruntime140.dll','ucrtbase.dll']
upx_exclus = ' '.join(['--upx-exclude=' + j for j in dll_exclus])

choice = easygui.boolbox(msg='是否要排除一些库', choices=['是Yes', '否No'])
if choice == True:
    py_used = easygui.multchoicebox(msg='请选择要打包脚本中使用的库', title='可多选', choices=py_lst)  # 3.10版本必须有title
    paichus = list(set(py_lst) - set(py_used))
    paichu = ' '.join(['--exclude-module=' + j for j in paichus])  # 排除的库
else:
    paichu = ''

daobao_lst = [dabao_python,dabao_pyinstall,upx_way,upx_exclus,paichu,file_way,ico,tmpdir_way,pyfile]
daobao_commond = ' '.join(daobao_lst)
pyperclip.copy(daobao_commond)
easygui.msgbox(msg='程序结束，请cmd到命令行模式，并cd进入到要打包脚本所在目录 粘贴后 运行')


