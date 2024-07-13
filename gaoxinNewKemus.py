'''
将001账套下会计科目与003账套下的会计科目进行比较，将001账套下有003账套下没有的会计科目显示出来

'''

import os
import pandas as pd
import easygui

# fname001 = r'F:\a00nutsrore\006\高新\001会计科目2024-1.xls'
fname001 = easygui.fileopenbox('请选择"001会计科目"excel文件')
path,filename = os.path.split(fname001)
os.chdir(path)
df001 = pd.read_excel(fname001,usecols=['科目编码','科目名称','助记码'])
df001['科目编码'] = df001['科目编码'].astype('string')
# fname003 = r'F:\a00nutsrore\006\高新\003会计科目202401.xls'
fname003 = easygui.fileopenbox('请选择"003会计科目"excel文件')
df003 = pd.read_excel(fname003,usecols=['科目编码','科目名称','助记码'])
df003['科目编码'] = df003['科目编码'].astype('string')
kemus01 = set()
for i in df001['科目编码'].to_list():
    kemus01.add(i)
kemus03 = set()
for i in df003['科目编码'].to_list():
    kemus03.add(i)
kemus = list(kemus01-kemus03)
df = df001[df001['科目编码'].isin(kemus)]
df.to_excel('新增会计科目.xlsx',index = False)
os.startfile('新增会计科目.xlsx')




