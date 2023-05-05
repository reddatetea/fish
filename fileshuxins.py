import openpyxl
import os
import easygui
import time
from xpinyin import Pinyin
import pandas as pd

path = r'D:\Kugou'
os.chdir(path)
filelst = [j for j  in os.listdir(path) if os.path.isfile(os.path.join(path,j))]
dic = {}
for j in filelst:
    filename,_ = os.path.splitext(j)
    suffix = _[1:]
    if suffix not in dic:
        dic[suffix]=[]
        dic[suffix].append(j)
    else :
        dic[suffix].append(j)
type_choices=list(dic.keys())
type_choices.sort()
print(type_choices)
mp3_files = dic['mp3']
sizes = [os.path.getsize(os.path.join(path,j)) for j in mp3_files]
atimes = [os.path.getatime(j) for j in mp3_files]  #查看文件的访问时间
ctimes = [os.path.getctime(j) for j in mp3_files]  #文件最后一次的改变时间
mtimes = [os.path.getmtime(j) for j in mp3_files]     #最近修改文件内容的时间
pinyin_files = [Pinyin().get_pinyin(j) for j in mp3_files]
df = pd.DataFrame({'文件名':mp3_files,'sizes':sizes,'atimes':atimes,'ctimes':ctimes,'mtimes':mtimes,'pinyinname':pinyin_files})
#df1 = df1.assign(ctimes=df1.ctimes.agg(lambda x:time.localtime(x)))   #time.localtime

def tihuan(x):
    gequ = x.split('-')[-1]
    geshou = x.split('-')[0]
    return gequ,geshou

df = df.assign(歌曲名=df['文件名'].str.replace('.mp3','').agg(tihuan(lambda x:tihuan(x)[0])))
path = r'f:\a00nutstore\fishc'
os.chdir(path)
df.to_excel('kkkkkkkk3.xlsx','aaa',index=False)