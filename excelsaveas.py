import  xlwings as xw
import os
import easygui

def excelSaveas(fname):
    qian,filehouzui = os.path.splitext(fname)
    app = xw.App(visible = False,add_book = False)
    wb = app.books.open(fname)
    sheets = wb.sheets
    sheetnames = [j.name for j in  sheets]
    msg = '请选择要保留的工作表'
    print(msg)

    baoliu_names = easygui.multchoicebox(msg,title = 'sheet',choices =sheetnames)

    delete_names = list(set(sheetnames)-set(baoliu_names))



    for delete_name in delete_names:

        sheets[delete_name].delete()

    msg = '请点选要欲往路径'
    print(msg)
    newpath = easygui.diropenbox(msg, title='请选文件夹')
    msg = '请输入文件新名字chuku10'
    newname = easygui.enterbox(msg, title='不用输后缀')
    newfilename = newname + filehouzui
    newfname = os.path.join(newpath, newfilename)


    wb.save(newfname)
    wb.close()
    app.quit()

    return newfname

def  main():

    msg = '请点选要需要另存为的excel文件'
    print(msg)
    fname = easygui.fileopenbox(msg,title='excel文件')
    path,filename = os.path.split(fname)
    os.chdir(path)
    excelSaveas(fname)


if __name__ == '__main__':
    main()

