import easygui
import openpyxl
import os

def shouxine(fname):
    shouxine_dic = {}
    wb = openpyxl.load_workbook(fname)
    ws=wb['授信额']
    for row in list(ws.values)[1:]:  # 按行读取ws工作表除表头外的所有数据。
        if not row[1] in shouxine_dic.keys():  # 如果row[0]在dic字典中不存在。
            shouxine_dic[row[1]] = row[2]

        else:  # 否则。
            continue


    wb.save(fname)  # 另存工作簿。
    return shouxine_dic




def main():
    msg = '请点选供应商授信额文件'
    fname = easygui.fileopenbox(msg)
    shouxine_dic = shouxine(fname)
    print(shouxine_dic)
    for key, value in shouxine_dic.items():  # 获取dic字典中的键和值，并赋值给对应的key和item。
        print(key, value)


if __name__ == '__main__':
    main()