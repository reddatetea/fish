'''
指定文件夹，按指定数目分割文件夹的文件
'''


import os
import easygui
import pandas as pd

def segmentation(path,num):
    lst = os.listdir(path)
    df1 = pd.DataFrame(data = lst,index = range(len(lst)))
    leibie = pd.cut(df1.index,bins=range(0,len(lst)+num,num),right = False)
    df2 = pd.DataFrame(leibie,index=range(len(leibie)),columns=['leibie'])
    df3 = pd.concat([df2,df1],axis=1)
    df3 = df3.astype({'leibie':str})
    df3.leibie = df3.leibie.str.strip()
    df3.leibie = df3.leibie.str.replace('[','')
    df3.leibie = df3.leibie.str.replace(')','')
    df3.dropna(inplace = True)
    df3.columns = ['leibie','shu']
    gp = df3.groupby('leibie',sort = False).shu.apply(list)
    n = len(str(len(lst)))
    
    for index,row in gp.items():
        a = str(index).split(',')
        name = a[0].strip().zfill(n) + '_' + a[-1].strip().zfill(n)
        dir_name = os.path.join(path,name)
        if os.path.exists(dir_name):
            continue
        else :
            os.mkdir(os.path.join(path,dir_name))
        for i in row:
           old_name = os.path.join(path,i)
           new_name = os.path.join(path,dir_name,i)
           os.rename(old_name,new_name)
 

def main():
    path = easygui.diropenbox('请点选文件路径')
    num = easygui.integerbox('请输入拆分文件的数量')
    segmentation(path,num)
    
if __name__ == '__main__':
    main()
    



