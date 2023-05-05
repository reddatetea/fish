import xlwings as xw
import pandas as pd
import excelmessage
import easygui
import os

def strToDatetime(fname):
    app = xw.App(visible = False,add_book = False)
    df = pd.read_excel(fname,dtype={'time':'datetime64[ns]'})
    df = df.set_index('入库日期')
    wb=app.books.add()
    ws=wb.sheets.active

    ws.range('a1').value = df
    wb.save(fname)
    app.quit()
    return fname

def main():
    msg = '请点选要转换为datetime 的excel文件'
    print(msg)
    fname = easygui.fileopenbox(msg)
    path,houzhui = os.path.splitext(fname)
    os.chdir(path)

    if houzhui=='.xlsx':
        fname = fname
    else :
        fname = fname + 'x'

    fname = strToDatetime(fname)

if __name__=='__main__':
    main()