import pandas as pd
import numpy as np

data_dict = {"province":['河南','河北','河南','河南','河南','河北'],
       "month":['2月','1月','1月','5月','3月','2月'],
       "temperature":['43','23','34','32','23','45']
      }
df =pd.DataFrame(data_dict)
df.groupby('province').apply(lambda x :x.sort_values(by='month').
          assign(number_bool = lambda x:x.month.str[0].astype(int).diff()==1,
                 temperature_shift = lambda x:x.temperature.shift(1),
                 新增列 =lambda x:(x.temperature+'-'+x.temperature_shift)[x.number_bool],
                 diff= lambda x:x.temperature.astype(float)-x.temperature_shift.astype(float))).sort_index(level=1).drop(['number_bool','temperature_shift'],axis=1).droplevel(0,axis=0)