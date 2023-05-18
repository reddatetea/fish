'''
applymap,Series的用法
'''
import pandas as pd
import string
print(pd.__version__)
df = pd.read_csv('https://www.gairuo.com/file/data/team.csv')
df = df.head()
df = pd.read_csv('https://www.gairuo.com/file/data/team.csv')
df = df.head()
# 将字母与 1-26 数字成对组合起来
str_map_temp = zip(string.ascii_uppercase, range(1, 27))
# 将 zip 对象转为字典，同时处理字母为字符，一位的向前补 0
str_map = {k:str(v).zfill(2) for k, v in str_map_temp}
def func(x):     #3.10版本可用:str|int
    # print(type(x), x)
    if isinstance(x, str):
        ser = pd.Series([*x])
        ser = ser.replace(str_map)
        return ''.join(ser)
    else:
        return x
df=df.applymap(func)
print(df)