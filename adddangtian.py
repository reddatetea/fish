import openpyxl
import datetime
import os
import shutil
import excelmessage

def addDangtian(oldname,fname):

    print('请点选原材料实时流水账.xlsx')
    #oldname = r'F:\a00nutstore\006\zw\原材料DDDDDDDDDDDDDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX实时流水账\原材料实时流水账.xlsx'

    #oldname = excelmessage.excelMessage()

    dangtianriqi = datetime.date.today().strftime('%Y%m%d')
    newname = oldname[:-5] + '副本' + dangtianriqi + '.xlsx'
    shutil.copyfile(oldname, newname)

    wb = openpyxl.load_workbook(oldname)
    #ws= wb.active
    ws = wb['流水账']        #以前版本是ws=wb.active,导致汇总工作表被挤占
    #fname = r'F:\a00nutstore\006\zw\原材料实时流水账\4.8流水账002.xlsx'
    wb1 = openpyxl.load_workbook(fname)
    ws1 = wb1.active

    for index, row in enumerate(ws1.values):
        if index == 0:
            continue
        else :
            ws.append(row)

    wb.save(oldname)
    wb1.close()
    return oldname

def main():
    fname = r'D:\a00002.xlsx'
    oldname = r'D:\a00nutstore\006\zw\原材料实时流水账\原材料实时流水账.xlsx'
    addDangtian(oldname,fname)

if __name__=='__main__':
    main()




