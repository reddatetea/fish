import pandas as pd
from io import StringIO
ts = '''
2020-10-28 09:59:44
2020-10-29 10:01:32
2020-10-30 10:04:27
2020-11-02 09:55:43
2020-11-03 10:05:03
2020-11-04 09:44:34
2020-11-05 10:10:32
2020-11-06 10:02:37
'''
df = pd.read_csv(StringIO(ts),names=['time'],parse_dates=['time'])
print(df)

ping_jun_shi_jian = df.time.apply(lambda s:s.replace(year=2000,month=1,day=1)).mean()
ping_jun_shi_jian = df.time.apply(pd.Timestamp.replace,year=2020,month=1,day=1).mean()
ping_jun_shi_jian = df.time.agg(pd.Timestamp.replace,year=2020,month=1,day=1).mean()
print(ping_jun_shi_jian)