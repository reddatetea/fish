import xlwings as xw
import pandas as pd
import os

fname = r'D:\a00nutstore\006\zw\2020\202009\2020入库.xlsx'
path,filename = os.path.split(fname)
data = pd.read_excel(fname)    #适合简单一个工作簿里只有一个工作表情形
#values = ws.range('A1').expand('table').options(pd.DataFrame).value     #可打开指定工作表并形成pd
gongyingshangs = list(data['供应商'].unique())
for gongyingshang in gongyingshangs:
    data_cut = data[data['供应商']==gongyingshang]
    data_cut.to_excel('.\%s.xlsx'%gongyingshang,index = False,encoding = 'utf-8')    #加index可去掉序号


