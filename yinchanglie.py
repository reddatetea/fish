'''
通过指定excel表的列名，对列进行隐藏
'''
import openpyxl
import easygui
import excelmessage

def yinchangLie(fname,ws_name='',lies=''):
    if lies == '':
        pass
    else :
        # fname = excelmessage.wenjian()
        fname = excelmessage.excelMessage(fname)
        wb = openpyxl.load_workbook(fname)
        if ws_name == '':
            ws = wb.active
        else :
            ws = wb[ws_name]
        for lie in lies:
            ws.column_dimensions['{}'.format(lie)].hidden = True

    wb.save(fname)
    return fname

def  main():
    msg = '请点选要隐藏列的excel文件'
    fname = easygui.fileopenbox(msg)
    ws_name = input('请输入要隐藏列的工作表\n')
    lies = input('请输入要隐藏列KLMN\n')
    yinchangLie(fname,ws_name,lies)


if __name__ == '__main__':
    main()


