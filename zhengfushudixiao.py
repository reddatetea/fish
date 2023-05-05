'''
正数负数相互抵消并删除
'''
import pandas as pd
from itertools import  pairwise

fname = r'F:\a00nutstore\fishc\正数负数相互抵消并删除.xlsx'
df = pd.read_excel(fname)

def grou_del_idex(grp):
    items = grp.TranAmt.items()
    del_idex = set()
    for i,nxt in pairwise(items):
        if i[1] + nxt[1] == 0 and i[0] not in del_idex and nxt[0] not in del_idex:
            del_idex.add(i[0])
            del_idex.add(nxt[0])
    return grp[~grp.index.isin(del_idex)]

df.groupby('Cat2',group_keys=False).apply(grou_del_idex)

print(df)

