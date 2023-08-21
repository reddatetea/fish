from io import StringIO
import pandas as pd
import numpy as np
import re
from sqlalchemy import true

data = '''
书单,作者,ISBN
资本论 1,袁某,23445-2342
资本论 2,袁某,23445-2342
资本论 3,袁某,23445-2342
大学语文 上,李四,a25245-32425
大学语文 下,李四,a25245-32425
数据结构,王某,x342w-ssa
'''
def mark(ser:pd.Series):
    if ser.isna().all():
        return  ''
    elif ser.str.isdecimal().all():
        return f'{ser.min()}-{ser.max()}'
    else :
        return ser.sum()

df = pd.read_csv(StringIO(data))
df1 = df.书单.str.split(' ',expand=True)
df1 = df1.set_axis(['书名','备注'],axis=1)
new_df = pd.concat([df,df1],axis=1)
result = new_df.groupby('书名',as_index=False,sort=False).agg({'作者':max,'ISBN':max,'备注':mark})
result
