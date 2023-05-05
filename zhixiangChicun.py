'''
根据纸箱字典制作纸箱尺寸EXCEL文件
'''
import os
import zhixiangTodic
import openpyxl
import easygui
import datetime

def chicun():
    zhixiang_dic = zhixiangTodic.zhixiangdic()
    path = r'f:\a00nutstore\006\zw\ZHIXIANG'
    os.chdir(path)

    dtrq = datetime.date.today().strftime('%Y%m%d')

    filename = '纸箱尺寸%s.xlsx'%dtrq
    fname = os.path.join(path,filename)
    wb = openpyxl.Workbook(fname)
    ws =wb.create_sheet(title = '纸箱尺寸')
    taitou = ('纸箱','长','宽','高')

    ws.append(taitou)

    for key,value in zhixiang_dic.items():
        print(key,value)
        hang = (key,value[0],value[1],value[2])
        ws.append(hang)

    wb.save(fname)

def main():
    chicun()

if __name__ == '__main__' :
    main()

