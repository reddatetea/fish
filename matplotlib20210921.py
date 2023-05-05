import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']    #支持中文
plt.rcParams['axes.unicode_minus']=False      #正常显示负号

fname = r'D:\a00nutstore\006\zw\else\销售明细20201226-20210917.xlsx'

# import numpy as np
cols = ['日期','发货数量','发货件数','发货价税合计原币','存货编码']
#,parse_dates=['日期']
df = pd.read_excel(fname,usecols=cols)
df1 = df.iloc[:24,:]
df1.plot(kind='line',title='发货件数折线图',xticks=np.arange(24))
plt.show()