import re
import pandas as pd
def addBen(string):
    pattern = r'(?P<num>\d+)本/件'
    regexp1 = re.compile(pattern)
    mat = regexp1.search(string)
    if mat:
        hanliang = int(mat.group('num'))
    else :
        hanliang  = 0
    return hanliang
fname_content = r"F:\programs\存货.xlsx"
df_content = pd.read_excel(fname_content)
df_content['content'] = df_content['计量单位'].map(addBen)
content_dic = dict(zip(df_content['存货编码'].to_list(),df_content['content'].to_list()))
print(content_dic)