import os
import pandas as pd
import pprint
import easygui
import xlwings as xw

def choicePath():                  #点选要删除文件所在的文件夹
    msg = '请点选想要搜索开始路径'
    title = '文件夹所在路径'
    easygui.msgbox(msg=msg,title=title)
    path = easygui.diropenbox(msg = msg,title = title)
    return path

def shangPath(path):
    os.chdir(path)
    # 上一级目录
    shang_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
    return shang_dir

def getnames(filenames,path):
    os.chdir(path)
    for eachfile in os.listdir(os.curdir):
        if os.path.isfile(eachfile):
            if '原材料盘存表' in eachfile:
                if eachfile.startswith('~'):
                    continue
                elif eachfile.endswith('xlsx'):
                    filenames.append(os.path.join(os.getcwd(), eachfile))
                elif eachfile.endswith('xls'):
                    filenames.append(os.path.join(os.getcwd(), eachfile))
                else :
                    continue


            else :
                continue
        else:
            filenames = getnames(filenames, eachfile)
            try:
                os.chdir(os.pardir)  # 递归调用后切记返回上一层目录
            except:
                print('已搜索到电脑的根目录')
    return filenames

def main():
    app = xw.App(visible=False, add_book=False)
    path = choicePath()
    os.chdir(path)
    shang_dir = shangPath(path)
    filenames = []
    filenames = getnames(filenames,path)
    data = []
    for j in filenames:
        print(j)
        wb = app.books.open(j)
        for i in wb.sheets:
            if 'AAA' in i.name :
                df = pd.DataFrame(pd.read_excel(j,i.name))
                data.append(df)
            else :
                continue
        wb.close()
    app.quit()
    datas = pd.concat(data)
    datas.dropna(subset=['品名'], inplace=True)  # 删除供货单位列中的有空值的行
    datas = datas[datas['品名'].str.contains('----------')==False]
    pinmings = datas['品名'].to_list()
    daleis = datas['存货大类名称'].to_list()
    pinming_dalei_dic = dict(zip(pinmings,daleis))
    df = pd.DataFrame(list(pinming_dalei_dic.items()),columns=['品名','存货大类名称'])
    fname = r'原材料品名大类字典.xlsx'
    with open('pinmingdaleiDic.py', 'w', encoding='utf-8') as f:
        f.write('pinming_dalei = ' + pprint.pformat(pinming_dalei_dic))
    df.to_excel(fname, '品名大类', index=False)
    os.startfile(fname)

if __name__ == '__main__':
    main()



